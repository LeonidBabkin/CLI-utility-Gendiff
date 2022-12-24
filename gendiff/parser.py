import json
import yaml
from os.path import splitext


def parse(content, ext):
    if ext == 'yaml' or ext == 'yml':
        output = yaml.safe_load(content)
        return output
    elif ext == 'json':
        output = json.loads(content)
        return output


def fetch_data(datum):
    _, extension = splitext(datum)
    with open(datum, 'r') as content:
        content = content.read()
    return parse(content, extension[1:])
