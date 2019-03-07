from setupy.core.model import Setup, Setting
from setupy.core.serialize import serialize_imports, \
                                  serialize_settings, \
                                  serialize_features


def test_serializer_can_serialize_with_imports():
    setup = Setup()
    setup.add_import("from setuptools import setup")
    setup.add_import("from setuptools import find_packages")
    setup.add_import("from os import path")
    setup.add_import("from io import open")

    assert serialize_imports(setup) == """from setuptools import setup
from setuptools import find_packages
from os import path
from io import open"""


def test_serializer_can_serialize_features():
    feature = """def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r"""

    setup = Setup()
    setup.add_feature(feature)
    setup.add_feature(feature)

    assert serialize_features(setup) == """def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r

def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r"""


def test_serializer_can_serialize_settings():

    setup = Setup()
    setup.add_setting(Setting('BASE', {
        "name": "\"setupy\"",
        "version": "\"0.1.0\"",
        "packages": "find_packages(exclude=['contrib', 'docs', 'test'])"
    }))

    assert serialize_settings(setup) == """BASE = {
    "name": "setupy",
    "version": "0.1.0",
    "packages": find_packages(exclude=['contrib', 'docs', 'test'])
}

setup(**merge(BASE))"""
