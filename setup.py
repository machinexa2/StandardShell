from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name = "standardshell",
    version = "1.0.2",
    author = "Machine Yadav",
    author_email = "machinexa@gmail.com",
    description = "Module for building shells",
    long_description = next(line.rstrip('\n') for line in open("README.md") if line),
    long_description_content_type = "text/markdown",
    url = "https://github.com/machinexa2/StandardShell",
    download_url = 'https://github.com/machinexa2/StandardShell/archive/v1.0.0.tar.gz',
    keywords  =  ['Python', 'Shell', 'RCE'],
    packages = ["standardshell"],
    include_package_data = True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.8',
    install_requires = [
        "interruptingcow"
    ],
)
