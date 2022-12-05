from gendiff.parser import parsing
from gendiff.formatters.internal_tree import build_ast
from gendiff.formatters.stylish import build_stylish


def generate_diff(path_to_file1, path_to_file2, output_format='stylish'):
    dict_before, dict_after = parsing(path_to_file1, path_to_file2)
    result_tree = build_ast(dict_before, dict_after)
    if output_format == 'stylish':
        result = build_stylish(result_tree)
    else:
        result = build_stylish(result_tree)
    return result.strip()
