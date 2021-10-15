from setuptools import setup
setup(
    name='homebrewery-to-enki',
    version='1.0.0',
    description='Converter between homebrewery and enki markdown formats.',
    url='https://github.com/lazy-scrivener-games/homebrewery-to-enki',
    author='Chris Muller',
    author_email='chris@lazyscrivenergames.com',
    license='MIT',
    packages=[
        'homebrewery-to-enki'
    ],
    scripts=[
        'scripts/homebrewery-to-enki'
    ],
    install_requires=[
    ]
)
