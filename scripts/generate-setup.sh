#!/bin/bash

env SETUPY_FEATURES=setupy/features \
SETUPY_SETTINGS=setupy/settings \
python -m setupy \
    -s base add_upload_command add_long_description \
    --include-setting "$(cat setupy.yaml)"
