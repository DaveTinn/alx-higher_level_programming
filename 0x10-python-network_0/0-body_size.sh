#!/bin/bash
# Script taking in a URL, sends a request to it, and displays the size of the body of the response.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f 2
