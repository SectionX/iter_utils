'''
Collection of iterators which attempt to flatten tree-like structures
like nested dictionaries, json and xml.
'''

from .src.flatten import flatten
from .src.flatten_xml import flatten_xml

__all__ = [
    'flatten',
    'flatten_xml'
]
