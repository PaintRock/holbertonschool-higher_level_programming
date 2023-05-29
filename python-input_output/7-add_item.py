#!/usr/bin/python3
"""Modulo: import 2 functions that create a json and a object"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:

    arg = sys.argv[1:]
    existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args)

    save_to_json_file(existing_list, "add_item.json")
