# 1. The dictionary value can be of any datatype
# 2. But, the dictionary key must be an immutable datatype

student = {"name": "jon", 2: 12, (1, 2): "Ram", 2.2: ["Harry", "Ram", "jon"]} # Valid dictionary
# invalid_d = {(1, 2): "sita", {1,2}: 12, ([1,2], 3): "Ram"} # Invalid dictionary
# Tuple can be used as keys, if they contain only immutable objects.If a tuple contains any
# mutable objects either directly or indirectly, it cannot be used as keys.
