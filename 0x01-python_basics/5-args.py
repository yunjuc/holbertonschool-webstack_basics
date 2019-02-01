#!/usr/bin/python3
import sys

n = len(sys.argv)

if __name__ == "__main__":
    if n == 1:
        print("0 argument.")
    else:
        if n == 2:
            print("{} argument:".format(n-1))
        else:
            print("{} arguments:".format(n-1))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
