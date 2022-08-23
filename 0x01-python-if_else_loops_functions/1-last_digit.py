#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if lastd > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastd))
elif lastd == 0:
    print("Last digit of {} is {} and is 0".format(number, lastd))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastd))
