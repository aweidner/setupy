from setuptools import find_packages, setup


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
    "version": open("VERSION.txt").read()
}

setup(**merge(base, setupy))
