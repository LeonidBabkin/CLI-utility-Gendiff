# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.generate_diff import generate_diff
import tests.expected as expected


def test_plain():
    result = generate_diff('./gendiff/fixtures/big1.json',
                           './gendiff/fixtures/big2.json',
                           'json')
    assert result == expected.JSON
