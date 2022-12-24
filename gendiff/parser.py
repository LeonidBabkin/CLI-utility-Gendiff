import json
import yaml


def parse(content, ext):
    if ext == 'yaml' or ext == 'yml':
        output = yaml.safe_load(content)
        return output
    elif ext == 'json':
        output = json.loads(content)
        return output
