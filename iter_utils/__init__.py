import io
import typing
import collections
from xml.etree.ElementTree import ElementTree

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
        }
    }

    Example output:
    ('key1', 'value1')
    ('key2.key2_1', 'value2_1_1')
    ('key2.key2_2', 'value2_2_1')

    Arguments:
    dictionary: The dict object or a dict-like object that implements the .items() method.
    namespace_separator: The character seperating the parent from the child. Default is '.'

    properties:
    length: Counts yields. Common use case is a sanity check when transforming 
            nested formats into predefined tables.

    '''
    def __init__(self, dictionary: dict[typing.Any, typing.Any], namespace_separator: str = '.'):
        self._dict = dictionary
        self.ns_sep = namespace_separator
        self._length = 0

    def __iter__(self):
        obj = self._dict
        sep = self.ns_sep
        queue = collections.deque()

        for k_outer, v_outer in obj.items():
            queue.appendleft((k_outer, v_outer, ''))
            while queue:
                k, v, namespace = queue.pop()

                if namespace:
                    namespace = f'{namespace}{sep}{k}'
                else:
                    namespace = k

                if isinstance(v, type(obj)):
                    for _k, _v in v.items():
                        queue.appendleft((_k, _v, namespace))
                else:
                    self._length += 1
                    yield namespace, v
    
    @property
    def length(self):
        return self._length


















class flatten_xml:

    def __init__(self, document: str | bytes | typing.IO | ElementTree, namespace_separator: str = '.'):
        if isinstance(document, ElementTree):
            self._doc = document
        elif isinstance(document, io.IOBase):
            self._doc = ElementTree(file=document)
        elif isinstance(document, str):
            self._doc = ElementTree(file=io.BytesIO(document.encode()))
        elif isinstance(document, bytes):
            self._doc = ElementTree(file=io.BytesIO(document))

        try:
            self._root = self._doc.getroot()
        except AttributeError as e:
            e.add_note('Could not transform document into an ElementTree.')
            raise e

        self._length = 0
        self.ns_sep = namespace_separator

    def __iter__(self):
        obj = self._root
        sep = self.ns_sep
        update_namespace = lambda self, seperator, tag: f'{self}{seperator}{tag}' if self else tag
        queue = collections.deque()
        
        for elem in obj:
            queue.appendleft((elem, obj.tag))
            

            while queue:
                element, namespace = queue.pop()
                namespace = update_namespace(namespace, sep, element.tag)
                if len(element):
                    for _elem in element:
                        queue.appendleft((_elem, namespace))
                else:
                    self._length += 1
                    yield namespace, element.text



    