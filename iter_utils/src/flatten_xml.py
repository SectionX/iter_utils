'''
Implementation of a flattening algorithm for xml.
Returns all elements under a string namespace.
'''

import io
import typing
import collections
from xml.etree.ElementTree import ElementTree


class flatten_xml:

    def __init__(self,
                 document: str | bytes | typing.IO | ElementTree,
                 namespace_separator: str = '.'):

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
            raise AttributeError(
                'Could not transform document into an ElementTree.'
                ) from e

        self._length = 0
        self.ns_sep = namespace_separator

    @property
    def length(self):
        return self._length

    def _update_namespace(self, namespace, seperator, tag):
        if namespace:
            return f'{namespace}{seperator}{tag}'
        return tag

    def __iter__(self):
        obj = self._root
        sep = self.ns_sep
        queue = collections.deque()

        for elem in obj:
            queue.appendleft((elem, obj.tag))

            while queue:
                element, namespace = queue.pop()
                namespace = self._update_namespace(namespace, sep, element.tag)
                if len(element):
                    for _elem in element:
                        queue.appendleft((_elem, namespace))
                else:
                    self._length += 1
                    yield namespace, element.text
