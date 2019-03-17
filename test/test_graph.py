from setupy.core.graph import Setup
from setupy.core.feature import Feature
from setupy.core.setting import Setting


class MockDependencyLoader:

    def __init__(self, features={}, settings={}):
        self._features = features
        self._settings = settings

    def load_feature(self, feature_name):
        return self._features[feature_name]

    def load_setting(self, setting_name):
        return self._settings[setting_name]

    def a_feature(self, feature_name, imports=[], features=[]):
        test_feature = Feature(feature_name, {
            "imports": imports,
            "features": features
        })

        self._features[feature_name] = test_feature

    def a_setting(self, setting_name, imports=[], features=[], settings=[]):
        test_setting = Setting(setting_name, {}, {
            "imports": imports,
            "features": features,
            "settings": settings
        })

        self._settings[setting_name] = test_setting


def test_graph_should_be_able_to_load_feature_with_import_dependencies():
    mdl = MockDependencyLoader()
    mdl.a_feature("test", ["from setuptools import setup"])

    g = Setup(mdl)
    g.add_feature("test")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test")}


def test_graph_should_produce_the_minimal_import_dependency_set():
    mdl = MockDependencyLoader()
    mdl.a_feature("test", ["from setuptools import setup"])
    mdl.a_feature("test2", ["from setuptools import setup"])

    g = Setup(mdl)
    g.add_feature("test")
    g.add_feature("test2")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test"), Feature("test2")}


def test_graph_should_import_feature_with_feature_dependencies():
    mdl = MockDependencyLoader()
    mdl.a_feature("test", features=["test2"])
    mdl.a_feature("test2", imports=["from setuptools import setup"])

    g = Setup(mdl)
    g.add_feature("test")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test"), Feature("test2")}


def test_graph_should_import_setting_with_import_dependencies():
    mdl = MockDependencyLoader()
    mdl.a_setting("test", imports=["from setuptools import setup"])

    g = Setup(mdl)
    g.add_setting("test")

    assert g.imports == {"from setuptools import setup"}
    assert g.settings == [Setting("test")]


def test_graph_should_import_setting_with_feature_dependencies():
    mdl = MockDependencyLoader()
    mdl.a_setting("test", features=["test2"])
    mdl.a_feature("test2", imports=["from setuptools import setup"])

    g = Setup(mdl)
    g.add_setting("test")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test2")}
    assert g.settings == [Setting("test")]


def test_graph_should_produce_minimal_feature_dependency_set_by_name():
    mdl = MockDependencyLoader()
    mdl.a_setting("test", features=["test3"])
    mdl.a_feature("test2", features=["test3"])
    mdl.a_feature("test3", imports=["from setuptools import setup"])

    g = Setup(mdl)
    g.add_setting("test")
    g.add_feature("test2")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test2"), Feature("test3")}
    assert g.settings == [Setting("test")]


def test_graph_should_produce_minimal_setting_dependency_set_by_name():
    mdl = MockDependencyLoader()
    mdl.a_setting("test")

    g = Setup(mdl)
    g.add_setting("test")
    g.add_setting("test")

    assert g.settings == [Setting("test")]


def test_adding_cyclical_feature_dependencies_is_fine():
    mdl = MockDependencyLoader()
    mdl.a_feature("test", features=["test2"])
    mdl.a_feature("test2", features=["test3"])
    mdl.a_feature("test3", features=["test"])

    g = Setup(mdl)
    g.add_feature("test")

    assert g.features == {Feature("test"), Feature("test2"), Feature("test3")}
