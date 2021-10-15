"""
Converts a Homebrewery-formatted markdown input to an enki-compatible one

usage: homebrewery-to-enki <input string>
"""
import sys

def main():
    """
    Converts a Homebrewery-formatted markdown input to an enki-compatible one.
    """
    text = sys.stdin.read()
    lines = text.split('\n')
    output = ''
    for line in lines:
        line = line.replace('\r', '')
        if line.startswith('{{'):
            line_output = parse_double_curly_brace_start(line)
        elif line.startswith('}}'):
            line_output = '</div>'
        elif line == ':':
            line_output = ''
        elif line == '\\page':
            # line_output = '<div style="page-break-after: always" markdown="1"></div>'
            line_output = ''
        else:
            line_output = line
        output += f'{line_output}\n'
    print(output)

def parse_double_curly_brace_start(line: str) -> str:
    """
    Converts double curly brace Homebrewery format to a div tag.
    """
    line = line[2:]
    if line.endswith('}}'):
        return ''
    if ':' in line:
        return f'<div style="{line}" markdown="1">'
    class_list = line.split(',')
    class_list.append('block')
    class_string = ' '.join(class_list)
    return f'<div class="{class_string}" markdown="1">'

if __name__ == '__main__':
    main()
