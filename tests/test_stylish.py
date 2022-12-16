# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.gendiff import generate_diff
import tests.expected as expected


def test_big_string_json():
    result = generate_diff('./tests/fixtures/big1.json',
                           './tests/fixtures/big2.json',
                           'stylish')
    assert result == expected.BIG_STRING


def test_small_string_json():
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'stylish')
    assert result == expected.SMALL_STRING


def test_big_string_yaml():
    result = generate_diff('./tests/fixtures/big1.yaml',
                           './tests/fixtures/big2.yaml',
                           'stylish')
    assert result == expected.BIG_STRING


def test_small_string_yaml():
    result = generate_diff('./tests/fixtures/file1.yaml',
                           './tests/fixtures/file2.yaml',
                           'stylish')
    assert result == expected.SMALL_STRING
