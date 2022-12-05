from gendiff.formatters.constants import INDENT


def gain_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def get_descendants(data, depth):
    subtree = ['{\n']
    for i in data:
        if not isinstance(data[i], dict):
            subtree.append(f'{INDENT * depth}    {i}: {gain_value(data[i])}\n')
        else:
            subtree.append(f'{INDENT * depth}    {i}: ')
            subtree.append(get_descendants(data[i], depth + 4))
    subtree.append(((INDENT * depth) + '}' + '\n'))
    return ''.join(subtree)


def build_stylish(data, depth=0):
    tree = ['{\n']
    for i in data:
        if isinstance(i['descendants'], list):
            tree.append(f'{INDENT * depth}  {i["state"]} {i["key"]}: ')
            tree.append(build_stylish(i['descendants'], depth + 4))
        elif isinstance(i['value'], dict):
            tree.append(f'{INDENT * depth}  {i["state"]} {i["key"]}: ')
            tree.append(get_descendants(i['value'], depth + 4))
        else:
            tree.append(f'{INDENT * depth}  {i["state"]} {i["key"]}: ' \
                    f'{gain_value(i["value"])}\n')
    tree.append(((INDENT * depth) + '}' + '\n'))
    return ''.join(tree)
