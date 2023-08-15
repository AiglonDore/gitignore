from setuptools import setup, find_packages
from core.help import VERSION

setup(
    name="gitignore",
    version=VERSION,
    description="A simple command line tool to generate .gitignore files",
    author="Aiglon Doré",
    author_email='aiglondore@outlook.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=open('requirements.txt').readlines(),
    packages=find_packages(),
)
    