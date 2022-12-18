# -*- coding: utf-8 -*-

"""Expected result constants."""


SMALL_STRING = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


BIG_STRING = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


BIG_PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


SMALL_PLAIN = '''Property 'follow' was removed
Property 'proxy.123.234.53' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''


SMALL_JSON = '''[{"key": "follow", "value": false, "state": "-", "descendants": ""}, {"key": "host", "value": "hexlet.io", "state": " ", "descendants": ""}, {"key": "proxy", "value": "123.234.53.22", "state": "-", "descendants": ""}, {"key": "timeout", "value": 50, "state": "-", "descendants": ""}, {"key": "timeout", "value": 20, "state": "+", "descendants": ""}, {"key": "verbose", "value": true, "state": "+", "descendants": ""}]'''


BIG_JSON = '''[{"key": "common", "value": "", "state": " ", "descendants": [{"key": "follow", "value": false, "state": "+", "descendants": ""}, {"key": "setting1", "value": "Value 1", "state": " ", "descendants": ""}, {"key": "setting2", "value": 200, "state": "-", "descendants": ""}, {"key": "setting3", "value": true, "state": "-", "descendants": ""}, {"key": "setting3", "value": null, "state": "+", "descendants": ""}, {"key": "setting4", "value": "blah blah", "state": "+", "descendants": ""}, {"key": "setting5", "value": {"key5": "value5"}, "state": "+", "descendants": ""}, {"key": "setting6", "value": "", "state": " ", "descendants": [{"key": "doge", "value": "", "state": " ", "descendants": [{"key": "wow", "value": "", "state": "-", "descendants": ""}, {"key": "wow", "value": "so much", "state": "+", "descendants": ""}]}, {"key": "key", "value": "value", "state": " ", "descendants": ""}, {"key": "ops", "value": "vops", "state": "+", "descendants": ""}]}]}, {"key": "group1", "value": "", "state": " ", "descendants": [{"key": "baz", "value": "bas", "state": "-", "descendants": ""}, {"key": "baz", "value": "bars", "state": "+", "descendants": ""}, {"key": "foo", "value": "bar", "state": " ", "descendants": ""}, {"key": "nest", "value": {"key": "value"}, "state": "-", "descendants": ""}, {"key": "nest", "value": "str", "state": "+", "descendants": ""}]}, {"key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "state": "-", "descendants": ""}, {"key": "group3", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "state": "+", "descendants": ""}]'''
