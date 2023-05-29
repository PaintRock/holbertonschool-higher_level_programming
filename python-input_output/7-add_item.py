#!/usr/bin/python3
"""Modulo: import 2 functions that create a json and a object"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:

    """Extract command-line arguments (excluding the script name)"""
    arg = sys.argv[1:]

    """Load existing list from file if it exists or initialize an empty list"""
    existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    """Add command-line arguments to the existing list"""
    existing_list.extend(args)

    """Save the updated list to the file"""
    save_to_json_file(existing_list, "add_item.json")

