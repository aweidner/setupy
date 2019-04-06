#!/bin/bash

python -m setupy \
    -s base add_upload_command add_long_description \
    --include-setting "$(cat setupy.yaml)"
