from os import path

from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r


base = {
    "name": "mypackage",
    "version": "0.1.0",
    "packages": find_packages(exclude=['contrib', 'docs', 'test'])
}

setupy = {
    "name": "setupy",
    "version": open("VERSION.txt").read(),
    "long_description": long_description,
    "install_requires": ["isort>=4.3", "pyyaml>=3.13", "flask>=1.0.2"],
    "extras_require": {
        "dev": ["pytest", "pytest-cov"],
        "neovim": ["neovim"]
    }
}



setup(**merge(base, setupy))
