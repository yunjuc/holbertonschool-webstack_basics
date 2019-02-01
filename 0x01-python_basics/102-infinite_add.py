#!/usr/bin/python3
import sys

res = 0

if __name__ == ("__main__"):
    if len(sys.argv) is 1:
        print(res)
    else:
        for i in range(1, len(sys.argv)):
            res += int(sys.argv[i])
        print(res)
