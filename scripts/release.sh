#!/bin/bash

python setup.py upload
./scripts/build-container.sh
./scripts/push-container.sh
