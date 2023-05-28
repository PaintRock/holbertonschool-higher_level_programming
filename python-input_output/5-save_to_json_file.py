#!/usr/bin/python3
"""retrn the JSON reperesentation of an object string"""
import json


def save_to_json_file(my_obj, filename):
    """Appends a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
