from setupy.core.feature import Feature
from setupy.core.setting import Setting
import yaml


class YamlDependencyLoader:

    def load_feature(self, contents, code):
        properties = yaml.load(contents)

        return Feature(
            properties["name"],
            properties.get("dependencies", {}),
            code)

    def load_setting(self, contents):
        properties = yaml.load(contents)
        return Setting(
            properties["name"],
            properties["properties"],
            properties.get("dependencies", {}))
