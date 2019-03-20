import os

from setupy.loaders import YamlDependencyLoader


class FileDependencyLoader:

    def __init__(self, feature_path, setting_path):
        self._feature_path = feature_path
        self._setting_path = setting_path
        self._yaml_loader = YamlDependencyLoader()

    def load_feature(self, feature_name):
        prefix = os.path.join(self._feature_path, feature_name)
        with open(prefix + ".yaml") as yaml:
            with open(prefix + ".py") as py:
                return self._yaml_loader.load_feature(yaml.read(), py.read())

    def load_setting(self, setting_name):
        with open(os.path.join(self._setting_path, setting_name) + ".yaml") as yaml:
            return self._yaml_loader.load_setting(yaml.read())
