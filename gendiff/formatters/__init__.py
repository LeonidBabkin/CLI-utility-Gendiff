from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain
from gendiff.formatters.json import build_json


def format_ast(ast, format_):
    if format_ == 'json':
        return build_json(ast).strip()
    elif format_ == 'plain':
        return build_plain(ast).strip()
    else:
        return build_stylish(ast).strip()
