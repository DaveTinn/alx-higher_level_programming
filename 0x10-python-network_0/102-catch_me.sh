#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message.
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
