from setupy.core.model import Setup
from setupy.core.serialize import serialize
from setupy.dependencies import FileDependencyLoader


def setupy(imports=None, features=None, settings=None, dependency_loader=FileDependencyLoader()):
    setup = Setup(dependency_loader)

    if (not features):
        features = []

    if (not imports):
        imports = []

    if (not settings):
        settings = []

    for i in imports:
        setup.add_import(i)
    for f in features:
        setup.add_feature(f)
    for s in settings:
        setup.add_setting(s)

    return serialize(setup)
