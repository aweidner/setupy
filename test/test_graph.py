from setupy.core.graph import SetupGraph
from setupy.core.feature import Feature
from contextlib import contextmanager


class MockDependencyLoader:

    def __init__(self, features={}):
        self._features = features

    def load_feature(self, feature_name):
        return self._features[feature_name]

    def a_feature_with_import(self, feature_name, imports):
        test_feature = Feature(feature_name, {
            "imports": imports
        })

        self._features[feature_name] = test_feature


def test_graph_should_be_able_to_load_feature_with_import_dependencies():
    mdl = MockDependencyLoader()
    mdl.a_feature_with_import("test", ["from setuptools import setup"])

    g = SetupGraph(mdl)
    g.add_feature("test")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test")}


def test_graph_should_produce_the_minimal_import_dependency_set():
    mdl = MockDependencyLoader()
    mdl.a_feature_with_import("test", ["from setuptools import setup"])
    mdl.a_feature_with_import("test2", ["from setuptools import setup"])

    g = SetupGraph(mdl)
    g.add_feature("test")
    g.add_feature("test2")

    assert g.imports == {"from setuptools import setup"}
    assert g.features == {Feature("test"), Feature("test2")}


def test_graph_should_import_feature_with_feature_dependencies():
    pass


def test_graph_should_import_setting_with_import_dependencies():
    pass


def test_graph_should_import_setting_with_feature_dependencies():
    pass


def test_graph_should_produce_minimal_feature_dependency_set_by_name():
    pass


def test_graph_should_import_setting_with_setting_dependencies():
    pass


def test_graph_should_produce_minimal_setting_dependency_set_by_name():
    pass


def test_graph_should_import_dependencies_recursively_and_reduce():
    pass


def test_graph_should_detect_cycles_and_throw_error():
    pass


def test_iterating_graph_should_produce_dependencies_in_reverse_topological_sort():
    pass
