#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num = len(argv) - 1
    if num == 0:
        print("{}".format(num))
    else:
        Sum = 0
        for i in range(1, num + 1):
            Sum += int(argv[i])
        print("{}".format(Sum))
