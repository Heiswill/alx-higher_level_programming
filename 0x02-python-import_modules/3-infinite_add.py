#!/usr/bin/python3
import sys

def add_arg(args):
    
    num = len(args) - 1
    if num == 0:
        print("{}".format(num))
        return
    elif num >= 2:
        Sum = 0
        for i in range(1, num + 1):
            Sum += int(args[i])
        print("{}".format(Sum))

if __name__ == "__main__":
    add_arg(sys.argv)
