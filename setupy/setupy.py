from setupy.core.model import Setup
from setupy.core.setting import Setting
from setupy.core.serialize import serialize
from setupy.util import short_unique


def get_base_settings():
    return {
        "name": "BASE",
        "properties": {
            "name": "\"mypackage\"",
            "version": "\"0.1.0\"",
            "packages": "find_packages(exclude=['contrib', 'docs', 'test'])"
        }
    }


def get_merge_feature():
    # TODO: Read this from file
    return """def merge(*dicts):
    r = {}
    for d in dicts:
        r.update(d)
    return r"""


def setupy(imports=None, features=None, settings=None):
    setup = Setup()

    if (not features):
        features = []

    features.insert(0, get_merge_feature())

    if (not imports):
        imports = []

    imports.insert(0, "from setuptools import find_packages")
    imports.insert(0, "from setuptools import setup")

    layer_names = ["BASE"]

    if (not settings):
        settings = []

    settings.insert(0, get_base_settings())

    converted_settings = []
    for item in settings:
        # TODO: Validate that no layer names conflict

        # TODO: Validate name is a valid python identifier
        name = item.get('name', short_unique(layer_names))
        layer_names.append(name)

        converted_settings.append(Setting(name, item.get('properties', {})))

    for i in imports:
        setup.add_import(i)
    for f in features:
        setup.add_feature(f)
    for s in converted_settings:
        setup.add_setting(s)

    return serialize(setup)
