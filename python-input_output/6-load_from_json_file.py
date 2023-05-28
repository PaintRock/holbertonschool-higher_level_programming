#!/usr/bin/python3
"""retrn the JSON reperesentation of an object string"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r', encoding="utf-8") as file:
       return json.loads(file.read())
