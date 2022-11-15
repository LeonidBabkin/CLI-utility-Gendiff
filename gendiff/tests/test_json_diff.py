# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.generate_diff import generate_diff
import tests.expected as expected


def test_json():
        result = generate_diff('./gendiff/fixtures/file1.json',
                './gendiff/fixtures/file2.json',
                'string')
        assert result == expected.JSON_STRING
