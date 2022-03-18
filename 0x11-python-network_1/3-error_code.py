#!/usr/bin/python3
""" print error code """
import urllib.request
import sys


if __name__ == "__main__":
    breq = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(breq)
        with urllib.request.urlopen(breq) as response:
            br = response.read().decode('utf-8')
            print(br)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
