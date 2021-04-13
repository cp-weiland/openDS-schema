#! /usr/bin/env python

import sys
import json, jsonschema

if len(sys.argv) > 2:
    (file, schema) = sys.argv[1], sys.argv[2]
    
else:
    file = "example-1.json"
    schema = "schema-1.json"

def load_json(jsonfoo):
    try:
        is_json = json.load(jsonfoo)
    except ValueError as e:
        return False
    return is_json

with open(file, 'r') as foo, open(schema, 'r') as sce: 
    try:
        jsonschema.validate(instance=load_json(foo), schema=load_json(sce))

    except jsonschema.exceptions.ValidationError as err:
        print("False")
        sys.exit(1)

print("Valid!")
