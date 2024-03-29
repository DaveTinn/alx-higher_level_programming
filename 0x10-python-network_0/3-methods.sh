#!/bin/bash
# Takes in URL and  displays all HTTP methods the server will accept.
curl -sI | grep 'Allow:' | cut -f2 -d' '
