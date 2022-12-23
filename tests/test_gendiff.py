import pytest
import os
from gendiff.gendiff import generate_diff
from tests import expected
from tests.tests_arguments import ARGS


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures/"


def build_fixture_path(fixture_name):
        return f'{FIXTURES_PATH}{fixture_name}'


@pytest.mark.parametrize('fst_fixture, snd_fixture, format_, output', ARGS)
def test_gendiff_formatters(fst_fixture, snd_fixture, format_, output):
    path_to_fst_fixture = build_fixture_path(fst_fixture)
    path_to_snd_fixture = build_fixture_path(snd_fixture)
    result = generate_diff(path_to_fst_fixture, path_to_snd_fixture, format_)
    assert result == output
