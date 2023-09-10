#!/bin/bash
docker rm -f checker
docker build -t checker:firstone .
docker run -p 9096:80 --rm --name checker checker:firstone
