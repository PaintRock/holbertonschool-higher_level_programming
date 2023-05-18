#!/usr/bin/python3
for first in range(0, 10):
    for last in range(first + 1, 10):
        if last == 8 and first == 9:
            print("{}{}".format(first, last))
else:
    print("{}{}".format(first, last), end=", ")