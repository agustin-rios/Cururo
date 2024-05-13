from setuptools import setup, find_packages

setup(
    name='cururo',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'PyGithub',
    ],
    entry_points={
        'console_scripts': [
            'cururo=src.cli:main',
        ],
    },
)
