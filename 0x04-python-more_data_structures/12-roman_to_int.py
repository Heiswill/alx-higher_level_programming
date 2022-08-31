#!/usr/bin/python3
def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def roman_to_int(roman_string):
    res = 0
    i = 0

    rn = roman_string
    while (i < len(rn)):
        s1 = value(rn[i])
        if (i + 1 < len(rn)):
            s2 = value(rn[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res
