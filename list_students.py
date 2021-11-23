import json
import os, sys

# path from user: python test_students.py path
path = sys.argv[1]

def list_students():
    print('A LIST OF ALL STUDENTS:\n')
    json_files = os.listdir(path)
    for json_file in json_files:
        with open(os.path.join(path, json_file)) as jfile:
            jdata = json.load(jfile)
        if "name" in jdata.keys():
            print(jdata["name"])
        else:
            print('The file', json_file, 'does not contain a "name"')
        print(len(jdata["name"])*'-')

list_students()
