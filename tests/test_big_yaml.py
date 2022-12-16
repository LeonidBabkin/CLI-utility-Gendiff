# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.gendiff import generate_diff
import tests.expected as expected


def test_big_yaml():
    result = generate_diff(
            './tests/fixtures/big1.yaml',
            './tests/fixtures/big2.yaml',
            'yaml')
    assert result == expected.BIG_YAML
