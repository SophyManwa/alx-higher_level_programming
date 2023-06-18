#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    result = 0
    for i in n:
        result += i
    return result
