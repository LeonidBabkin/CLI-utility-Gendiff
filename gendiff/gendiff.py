from gendiff.formatters import format_ast
from gendiff.formatters.internal_tree import build_ast
from gendiff.parser import fetch_data


def generate_diff(path_to_file1, path_to_file2, format_='stylish'):
    fst_content = fetch_data(path_to_file1)
    snd_content = fetch_data(path_to_file2)
    ast = build_ast(fst_content, snd_content)
    result = format_ast(ast, format_)
    return result
