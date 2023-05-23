#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        for key in sorted(a_dictionary):
            print("{}: {}".format(key, a_dictionary[key]))
    else:
        print("None")
