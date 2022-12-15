from gendiff.parser import parsing
from gendiff.formatters.internal_tree import build_ast
from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain
from gendiff.formatters.json import build_json

def generate_diff(path_to_file1, path_to_file2, output_format='stylish'):
    dict_before, dict_after = parsing(path_to_file1, path_to_file2)
    ast = build_ast(dict_before, dict_after)
    if output_format == 'plain':
        return build_plain(ast).strip()
    elif output_format == 'json':
        return build_json(ast).strip()
    else:
        return build_stylish(ast).strip()
