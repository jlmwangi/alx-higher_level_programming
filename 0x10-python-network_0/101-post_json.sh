#!/bin/bash
# requests for contents of a JSON file
curl $1 -sX POST -H 'Content-Type: application/json" -d @$2
