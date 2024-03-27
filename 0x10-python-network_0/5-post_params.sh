#!/usr/bin/bash
# sends a post request to url

curl -s "$1" -X POST -d "email=test@gmail.com&subject=Iwill always be here for PLD"
