'''
Implementation of a flattening algorithm for nested dictionaries.
Returns all elements under a string namespace.
'''

import typing
import collections


class flatten:
    '''
    Iterator that flattens the nested contents of a python dictionary
    and assigns a namespace.

    usage:
    for k, v in flatten(dict_object):
        print(k, v)

    Example input:
    {
        'key1': 'value1',
        'key2': {
            'key2_1': 'value2_1_1',
            'key2_2': 'value2_2_1'
        },
        'key3': ['value3_1', 'value3_2']
    }

    Example output:
    ('key1', 'value1')
    ('key2.key2_1', 'value2_1_1')
    ('key2.key2_2', 'value2_2_1')
    ('key3, 'value3_1')
    ('key3, 'value3_2')

    Arguments:
    dictionary: The dict object or a dict-like
    object that implements the .items() method.
    namespace_separator: The character seperating
    the parent from the child. Default is '.'

    properties:
    length: Counts yields. Common use case is a
            sanity check when transforming nested
            formats into predefined tables.

    '''
    def __init__(self,
                 dictionary: dict[typing.Any, typing.Any],
                 namespace_separator: str = '.'):
        self._dict = dictionary
        self.ns_sep = namespace_separator
        self._length = 0

    def _update_namespace(self, namespace, seperator, key):
        if namespace:
            return f'{namespace}{seperator}{key}'
        return key

    def __iter__(self):
        obj = self._dict
        sep = self.ns_sep
        queue = collections.deque()

        for k_outer, v_outer in obj.items():
            queue.appendleft((k_outer, v_outer, ''))
            while queue:
                k, v, namespace = queue.pop()
                namespace = self._update_namespace(namespace, sep, k)

                if isinstance(v, dict):
                    for _k, _v in v.items():
                        queue.appendleft((_k, _v, namespace))
                else:
                    if not isinstance(v, list):
                        self._length += 1
                        yield namespace, v
                    else:
                        for item in v:
                            if isinstance(item, dict):
                                for _k, _v in item.items():
                                    queue.appendleft((_k, _v, namespace))
                            else:
                                self._length += 1
                                yield namespace, item

    @property
    def length(self):
        return self._length
