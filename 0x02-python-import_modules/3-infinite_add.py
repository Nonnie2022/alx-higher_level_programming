#!/usr/bin/python3
import sys

num = len(sys.argv)

if __name__ == "__main__":
    count = 0
    if num == 1:
        print(count)
    else:
        for i in range(1, num):
            count += int(sys.argv[i])
        print(count)
