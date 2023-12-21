from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Simple library to encrypt strings with MD5, SHA256 and SHA512 hashes'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="str-basic-encryption",
    version=VERSION,
    author="KidiXDev",
    author_email="<kidixdev@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/KidiXDev/str-basic-encryption',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['str', 'md5', 'sha256', 'sha512', 'encryption'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)