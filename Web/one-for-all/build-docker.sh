#!/bin/bash
docker rm -f oneforall 
docker build -t oneforall:firstone .
docker run -p 9090:9099 --rm --name oneforall oneforall:firstone
