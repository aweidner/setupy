from setuptools import setup
from setuptools import find_packages

def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r

BASE = {
    "name": "mypackage",
    "version": "0.1.0",
    "packages": find_packages(exclude=['contrib', 'docs', 'test'])
}

SETUPY = {
    "name": "setupy",
    "version": open("VERSION.txt").read()
}

setup(**merge(BASE, SETUPY))
