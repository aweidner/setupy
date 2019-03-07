
class Setting:

    def __init__(self, name, properties):
        self._name = name
        self._properties = properties

    @property
    def name(self):
        return self._name

    @property
    def properties(self):
        return self._properties


class Setup:

    def __init__(self):
        self._imports = []
        self._features = []
        self._settings = []

    def add_import(self, module):
        self._imports.append(module)

    def add_setting(self, setting):
        self._settings.append(setting)

    def add_feature(self, feature):
        self._features.append(feature)

    @property
    def imports(self):
        return self._imports

    @property
    def features(self):
        return self._features

    @property
    def settings(self):
        return self._settings
