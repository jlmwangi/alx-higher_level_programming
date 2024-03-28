#!/usr/bin/bash
# displays only the status code of respons
curl $1 -sI -w '%{http_code}' -o /dev/null
