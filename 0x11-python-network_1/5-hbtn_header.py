#!/usr/bin/python3
""" Module that displays value of variable X-Request-Id """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    ri = r.headers.get('X-Request-Id')
    print(ri)
