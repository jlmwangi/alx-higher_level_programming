#!/bin/bash
# displays body of a get request
curl -s "$1" -X GET -H "X-School-User-Id: 98"
