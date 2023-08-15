from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

setup(
    name="gitignore",
    version="1.0.0",
    description="A simple command line tool to generate .gitignore files",
    author="Aiglon Doré",
    author_email='aiglondore@outlook.com',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    packages=find_packages(),
)
    