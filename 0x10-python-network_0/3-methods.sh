#!/bin/bash
# displays all http metods the sever will accept
curl -sI "$1" | grep "Allow" | cut -f 2- -d' '
