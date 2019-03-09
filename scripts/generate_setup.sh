#!/bin/bash

python -m setupy \
    -s '{ "name": "SETUPY", "properties": { "name": "\"setupy\"", "version": "open(\"VERSION.txt\").read()" } }' \
    > setup.py
