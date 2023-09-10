#!/bin/bash
docker run -p 5001:5001 --privileged $(docker build -q .)
