import json
from pprint import pformat

def serialize(setup):
    imports = serialize_imports(setup)
    features = serialize_features(setup)
    settings = serialize_settings(setup)

    return f"{imports}\n\n{features}\n\n{settings}"


def serialize_imports(setup):
    return "\n".join(setup.imports)


def serialize_features(setup):
    return "\n\n".join(setup.features)


def serialize_settings(setup):
    settings = setup.settings

    settings_as_dictionaries = (to_dictionary(s) for s in settings)

    serialized_settings = "\n\n".join(settings_as_dictionaries)
    setting_names = ", ".join(s.name for s in settings)
    setup_line = f"setup(**merge({setting_names}))"

    return f"{serialized_settings}\n\n{setup_line}"


def to_dictionary(setting):
    name = setting.name
    dictionary = pretty(setting.properties)
    return f"{name} = {{\n{dictionary}\n}}"


def pretty(d, indent=1):
    result = []
    for key, value in d.items():
        tabs = " " * indent * 4
        formatted_value = value
        if isinstance(formatted_value, dict):
            formatted_value = pretty(value)

        line = f'{tabs}"{key}": {formatted_value}'
        result.append(line)
    return ",\n".join(result)
