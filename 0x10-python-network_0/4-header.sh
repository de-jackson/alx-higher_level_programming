#!/bin/bash
# Send GET request and displays body of reponse
curl -sX "GET" "$1" -H "X-School-User-Id: 98"
