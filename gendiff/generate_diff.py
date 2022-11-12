import json


def dct(dict1, dict2):
    dict3 = {}
    for i in sorted(dict1):
        if i in dict2:
            if dict1[i] == dict2[i]:
                dict3[f'  {i}'] = dict1[i]
            else:
                dict3[f'- {i}'] = dict1[i]
                dict3[f'+ {i}'] = dict2[i]
        if i not in dict2:
            dict3[f'- {i}'] = dict1[i]
    for i in sorted(dict2):
        if i not in sorted(dict1):
            dict3[f'+ {i}'] = dict2[i]
    return dict3


def generate_diff(path_to_file1, path_to_file2, out_format):
    with open(path_to_file1, 'r', encoding='utf-8') as datum1:
        dict1 = json.load(datum1)
    with open(path_to_file2, 'r', encoding='utf-8') as datum2:
        dict2 = json.load(datum2)
    dict3 = dct(dict1, dict2)
    path = 'gendiff/fixtures/result.json'
    out_file = open(path, "w")
    json.dump(dict3, out_file, indent=4, sort_keys=False)
    out_file.close()
    lst = []
    with open(path, 'r', encoding='utf-8') as datum3:
        for i in datum3.readlines():
            i = i.strip()
            i = i.replace('"', '')
            i = i.replace(',', '')
            lst.append(i)
    string = '\n  '.join(lst[:-1])
    return string + '\n}'
