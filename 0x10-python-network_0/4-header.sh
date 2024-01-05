#!/bin/bash
# sends A header variable X-School-User-Id must be sent with the value 98
curl -s $1 -H "X-School-User-Id: 98"
