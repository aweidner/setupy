#!/bin/bash
docker build -t setupy:$(cat VERSION.txt) .
docker build -t setupy:latest .
