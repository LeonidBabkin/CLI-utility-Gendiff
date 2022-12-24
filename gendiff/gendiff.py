from gendiff.formatters import format_ast
from gendiff.formatters.internal_tree import build_ast
from gendiff.parser import parse
from os.path import splitext


def fetch_data(datum):
    _, extension = splitext(datum)
    with open(datum, 'r') as content:
        content = content.read()
    return parse(content, extension[1:])


def generate_diff(path_to_file1, path_to_file2, format_='stylish'):
    fst_content = fetch_data(path_to_file1)
    snd_content = fetch_data(path_to_file2)
    ast = build_ast(fst_content, snd_content)
    result = format_ast(ast, format_)
    return result
