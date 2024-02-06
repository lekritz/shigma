from setuptools import setup, find_packages

import os


with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Allows for doing mathematical sigma and pi notation."

# Setting up
setup(
    name="shigma",
    version=VERSION,
    author="Lekritz (Henryk Popioɫek)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url="https://github.com/lekritz/shigma",
    license="M.I.T. License",
    install_requires=[],
    keywords=["python", "sigma", "pi", "maths", "math", "mathematics"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    python_requires=">=3.0"
)
