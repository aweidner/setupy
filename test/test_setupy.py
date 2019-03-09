from setupy.setupy import setupy


def test_can_produce_its_own_config():
    assert setupy(settings=[{
        "name": "SETUPY",
        "properties": {
            "name": "\"setupy\"",
            "version": "\"0.1.0\"",
        }
    }]) == """from setuptools import setup
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
    "version": "0.1.0"
}

setup(**merge(BASE, SETUPY))"""
