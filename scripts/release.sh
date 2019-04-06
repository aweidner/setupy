#!/bin/bash

git push
python setup.py upload
./scripts/build-container.sh
./scripts/push-container.sh
