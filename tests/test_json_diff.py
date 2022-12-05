# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.generate_diff import generate_diff
import tests.expected as expected


def test_json():
    result = generate_diff(
            './gendiff/fixtures/big1.json',
            './gendiff/fixtures/big2.json',
            'string')
    assert result == expected.BIG_STRING
