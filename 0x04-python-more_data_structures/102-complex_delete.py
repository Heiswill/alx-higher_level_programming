#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    uniq = []
    for key, keyvalue in a_dictionary.items():
        if keyvalue is value:
            uniq.append(key)
    for i in uniq:
        del a_dictionary[i]
    return a_dictionary
