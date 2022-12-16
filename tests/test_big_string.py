# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.gendiff import generate_diff
import tests.expected as expected


def test_big_string():
    result = generate_diff(
            './tests/fixtures/big1.json',
            './tests/fixtures/big2.json',
            'string')
    assert result == expected.BIG_STRING
