#!/usr/bin/python3
"""retrn the JSON reperesentation of an object string"""


def to_json_string(my_obj):
    """Appends a file"""
    try:
        json_string = str(my_obj).replace("'", '"')
        return json.str
    except Exception:
        return None
