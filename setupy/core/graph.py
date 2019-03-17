
class SetupGraph():

    def __init__(self, dependency_loader):
        self._dependency_loader = dependency_loader

        self._adjacent = {}

        self._imports = set()
        self._features = set()

    def add_import(self, _import):
        self._imports.add(_import)
        return _import

    def add_feature(self, feature_name):
        feature = self._dependency_loader.load_feature(feature_name)
        if not self._adjacent.get(feature.name):
            self._adjacent[feature.name] = set()

        self._load_dependant_features(feature)
        self._load_dependant_imports(feature)

        self._features.add(feature)

    def _load_dependant_features(self, feature):
        for f_name in feature.dependant_features:
            dep_feature = self.add_feature(f_name)
            self._adjacent[feature.name].add(dep_feature)

    def _load_dependant_imports(self, feature):
        for i in feature.dependant_imports:
            dep_import = self.add_import(i)
            self._adjacent[feature.name].add(dep_import)

    @property
    def imports(self):
        return self._imports

    @property
    def features(self):
        return self._features
