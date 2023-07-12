#!/usr/bin/python3

""" module """


import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_list = []
try:
    my_list = load_from_json_file("add_item.json")
except Exception as e:
    pass
finally:
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
