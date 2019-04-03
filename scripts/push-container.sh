#!/bin/bash

docker tag setupy:$(cat VERSION.txt) aweidner/setupy:$(cat VERSION.txt)
docker push aweidner/setupy:$(cat VERSION.txt)

docker tag setupy:latest aweidner/setupy:latest
docker push aweidner/setupy:latest
