# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.generate_diff import generate_diff
import tests.expected as expected


def test_yaml():
    result = generate_diff(
            './gendiff/fixtures/file1.json',
            './gendiff/fixtures/file2.json',
            'string')
    assert result == expected.YAML_STRING
