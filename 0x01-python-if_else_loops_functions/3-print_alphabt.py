#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) not in ('q', 'e'):
        print("{}".format(chr(c)), end='')
