# pylint: disable=C0116

from iter_utils import flatten

nested_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': {
        'key3_1': 'value3_1',
        'key3_2': 'value3_2'
    },
    'key4': ['value4_1', 'value4_2'],
    'key5': {
        'key5_1': {
            'key5_1_1': 'value5_1_1'
        }
    },
    'key6': {
        'key6_1': ['value6_1_1', 'value6_1_2']
    },
    'key7': [
        {'key7_1': 'value7_1'},
        {'key7_2': 'value7_2'}
    ]

}

def test_flatten_length():
    results = []
    flattened = flatten(nested_dict)
    for k, v in flattened:
        results.append((k, v))

    assert len(results) == 11 == flattened.length, "wrong flatten length for flatten(dict)"

def test_flatten_objects():
    results = []
    for k in flatten(nested_dict):
        results.append(k)

    check_keys = ['key1', 'key2', 'key3.key3_1', 'key3.key3_2', 'key4', 'key4', 'key5.key5_1.key5_1_1', 'key6.key6_1', 'key6.key6_1', 'key7.key7_1', 'key7.key7_2']
    check_values = ['value1', 'value2', 'value3_1', 'value3_2', 'value4_1', 'value4_2', 'value5_1_1', 'value6_1_1', 'value6_1_2', 'value7_1', 'value7_2']
    check = [*zip(check_keys, check_values)]
    assert results == check, 'wrong key names for flatten(dict)'
