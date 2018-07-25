# Setup file for unificontrol
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unificontrol",
    version="0.1.0",
    author="Nicko van Someren",
    author_email="nicko@nicko.org",
    description="Secure access to Unifi network controllers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickovs/unificontrol",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
