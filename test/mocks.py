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

    def a_feature(self, feature_name, imports=[], features=[], code=""):
        test_feature = Feature(feature_name, {
            "imports": imports,
            "features": features
        }, code)

        self._features[feature_name] = test_feature

    def a_setting(self, setting_name, imports=[], features=[], settings=[], properties={}):
        test_setting = Setting(setting_name, properties, {
            "imports": imports,
            "features": features,
            "settings": settings
        })

        self._settings[setting_name] = test_setting
