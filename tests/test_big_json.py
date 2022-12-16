# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.gendiff import generate_diff
import tests.expected as expected


def test_big_json():
    result = generate_diff('./tests/fixtures/big1.json',
                           './tests/fixtures/big2.json',
                           'json')
    assert result == expected.BIG_JSON
