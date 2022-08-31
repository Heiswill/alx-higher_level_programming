#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
    return (biggest)
