#!/bin/bash

env SETUPY_FEATURES=setupy/features \
SETUPY_SETTINGS=setupy/settings \
python -m setupy \
    -s base \
    --include-setting "$(cat setupy.yaml)"
