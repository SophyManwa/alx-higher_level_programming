#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        result += uppercase_char
    print(result)
