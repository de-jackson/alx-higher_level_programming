#!/bin/bash
# Displays all acceptable HTTP methods
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
