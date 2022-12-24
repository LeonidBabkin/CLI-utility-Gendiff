from gendiff.formatters.constants import (ADDED,
                                          NESTED,
                                          REMOVED,
                                          UNCHANGED,
                                          WHITESPACE,
                                          NO_DESCENDANTS,
                                          )


def build_node(key, state, value, descendants):
    return {
        'key': key,
        'value': value,
        'state': state,
        'descendants': descendants,
    }


def build_ast(dict_before, dict_after):
    node = []
    removed = dict_before.keys() - dict_after.keys()
    added = dict_after.keys() - dict_before.keys()
    keys = sorted(dict_before.keys() | dict_after.keys())
    for key in keys:
        if key in removed:
            node.append(build_node(key, REMOVED, dict_before[key], NO_DESCENDANTS))
        elif key in added:
            node.append(build_node(key, ADDED, dict_after[key], NO_DESCENDANTS))
        elif dict_before[key] == dict_after[key]:
            node.append(build_node(key, UNCHANGED, dict_before[key], NO_DESCENDANTS))
        else:
            if isinstance(dict_before[key], dict) and \
                    isinstance(dict_after[key], dict):
                node.append(build_node(key, NESTED, WHITESPACE,
                            build_ast(dict_before[key], dict_after[key])))
            else:
                node.append(build_node(key, REMOVED, dict_before[key], NO_DESCENDANTS))
                node.append(build_node(key, ADDED, dict_after[key], NO_DESCENDANTS))
    return node
