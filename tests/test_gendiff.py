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


def test_big_plain_json():
    result = generate_diff('./tests/fixtures/big1.json',
                           './tests/fixtures/big2.json',
                           'plain')
    assert result == expected.BIG_PLAIN

def test_small_plain_json():
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json',
                           'plain')
    assert result == expected.SMALL_PLAIN


def test_big_plain_yaml():
    result = generate_diff('./tests/fixtures/big1.yaml',
                           './tests/fixtures/big2.yaml',
                           'plain')
    assert result == expected.BIG_PLAIN


def test_small_plain_yaml():
    result = generate_diff('./tests/fixtures/file1.yaml',
                           './tests/fixtures/file2.yaml',
                           'plain')
    assert result == expected.SMALL_PLAIN
    
    
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
