#!/usr/bin/python3
"""Modulo: import 2 functions that create a json and a object"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    lista = load_from_json_file("add_item.json")
except FileNotFoundError:
    lista = []

for element in sys.argv[1:]:
    lista.append(element)

save_to_json_file(lista, "add_item.json")
