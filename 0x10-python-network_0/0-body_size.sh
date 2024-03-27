#!/usr/bin/bash
# sends a request to a url

curl -w '%{size_download}\n' -so /dev/null $1
