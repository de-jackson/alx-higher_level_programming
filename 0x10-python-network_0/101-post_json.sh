#!/bin/bash
# sends JSON POST request to URL
curl -s -X POST $1 -d @"$2" --header "Content-Type: application/json"
