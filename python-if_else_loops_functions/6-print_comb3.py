#!/usr/bin/python3
for first in range(0, 10):
        for last in range(0, 10):
                    if last > first:
                                    if last > 8 and first > 7:
                                                        print("{}{}".format(first, last))
                                    else:
                                                        print("{}{}".format(first, last), end=", ")
