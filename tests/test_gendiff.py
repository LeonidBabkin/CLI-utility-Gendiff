import pytest
from tests.tests_arguments import ARGS, FIXTURE_PATH
from gendiff.gendiff import generate_diff


def build_fixture_path(fixture_name):
    return f'{FIXTURE_PATH}{fixture_name}'


@pytest.mark.parametrize('fst_fixture, snd_fixture, format_, output', ARGS)
def test_gendiff_formatters(fst_fixture, snd_fixture, format_, output):
    path_to_fst_fixture = build_fixture_path(fst_fixture)
    path_to_snd_fixture = build_fixture_path(snd_fixture)
    result = generate_diff(path_to_fst_fixture, path_to_snd_fixture, format_)
    assert result == output
