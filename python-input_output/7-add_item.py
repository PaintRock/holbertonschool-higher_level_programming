#!/usr/bin/python3
import json
"""Adds all args to a Python list and saves to a file"""


from save_to_json_file import 5-save_to_json_file
from load_to_json_file import 6-load_from_json_file

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

    existing_list.extend(args)

    save_to_json_file(existing_list, "add_item.json")
