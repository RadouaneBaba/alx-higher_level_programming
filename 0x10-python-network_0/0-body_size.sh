#!/bin/bash
# display size of the body of the response
curl -s -I $1 | grep 'Content-Length' | awk '{print $2}'
