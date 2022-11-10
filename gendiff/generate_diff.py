import os
import json


def generate_diff(path_to_file1, path_to_file2, out_format):
    with open(path_to_file1, 'r', encoding='utf-8') as datum1:
        dict1 = json.load(datum1)
    with open(path_to_file2, 'r', encoding='utf-8') as datum2:
        dict2 = json.load(datum2)

    dct3 = {}

    for i in sorted(dict1):
        if i in dict2:
            if dict1[i] == dict2[i]:
                dct3[f'  {i}'] = dict1[i]
            else:
                dct3[f'- {i}'] = dict1[i]
                dct3[f'+ {i}'] = dict2[i]
        if i not in dict2:
            dct3[f'- {i}'] = dict1[i]

    for i in sorted(dict2):
        if i not in sorted(dict1):
            dct3[f'+ {i}'] = dict2[i]
    return dct3    
    out_file = open(fixtures/result.json, "w")
    json.dump(dct3, out_file, indent = 4, sort_keys = False)
    out_file.close()

    with open(fixtures/result.json, 'r', encoding='utf-8') as datum3:
        for i in datum3.readlines():
            return i.strip()
