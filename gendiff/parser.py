import json
import yaml


def parsing(path_to_file1, path_to_file2):
    if path_to_file1.endswith('.json'):
        with open(path_to_file1, 'r', encoding='utf-8') as datum1:
            dict1 = json.load(datum1)
        with open(path_to_file2, 'r', encoding='utf-8') as datum2:
            dict2 = json.load(datum2)
    elif path_to_file1.endswith('.yaml') or path_to_file1.endswith('.yml'):
        with open(path_to_file1, 'r', encoding='utf-8') as datum1:
            dict1 = yaml.load(datum1, Loader=yaml.SafeLoader)
        with open(path_to_file2, 'r', encoding='utf-8') as datum2:
            dict2 = yaml.load(datum2, Loader=yaml.SafeLoader)
    return dict1, dict2
