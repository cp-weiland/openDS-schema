# openDS-schema

Examples for DS JSON serialization and corresponding JSON Schemas for validation corresponding to <https://github.com/DiSSCo/openDS/blob/master/basic-json-schema.md> (Schemas 1-3).

Could be used with a validator like [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/):

jsonschema -i example-1.json schema-1.json

Or the provided wrapper:

jsonval.py example-1.json schema-2.json\
Valid!

schema-4.json provides a simple pattern for the validation of accompanying media (images in example-SeSam-452904.json) and could be used for own extensions.



