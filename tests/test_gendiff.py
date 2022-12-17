from gendiff.gendiff import generate_diff
import tests.expected as expected


def test_big_json_json():
    result = generate_diff('./tests/fixtures/big1.json',
                           './tests/fixtures/big2.json',
                           'json')
    assert result == expected.BIG_JSON


def test_small_json_json():
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'json')
    assert result == expected.SMALL_JSON


def test_big_json_yaml():
    result = generate_diff('./tests/fixtures/big1.yaml',
                           './tests/fixtures/big2.yaml',
                           'json')
    assert result == expected.BIG_JSON


def test_small_json_yaml():
    result = generate_diff('./tests/fixtures/file1.yaml',
                           './tests/fixtures/file2.yaml',
                           'json')
    assert result == expected.SMALL_JSON
  
