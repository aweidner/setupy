class Feature:
    def __init__(self, name, dependencies={}):
        self._name = name
        self._dependencies = dependencies

    @property
    def name(self):
        return self._name

    @property
    def dependant_imports(self):
        return self._dependencies.get("imports", [])

    @property
    def dependant_features(self):
        return self._dependencies.get("features", [])

    def __eq__(self, other):
        return (isinstance(other, Feature) and
                other.name == self._name)

    def __hash__(self):
        return hash(self._name)
