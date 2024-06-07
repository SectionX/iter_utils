# description
Iterators for flattening tree-like / nested data structures  
into a namespace scheme.

Supports:
* python dicts
* xml with python's built-in xml module
* json with python's built-in json module.

# Installation:
pip install git+https://github.com/SectionX/iter_utils

# Documenation
Examples:  
python dictionary
```python  
from iter_utils import flatten

for k, v in flatten(dict_object):  
    ...
```
xml from file
```python
from iter_utils import flatten

with open('path/to/xml') as file:  
    for k, v in flatten_xml(file):  
        ...
```
xml from feed
```python
from iter_utils import flatten_xml
import requests

resp = requests.get('url/to/xml')
for k, v in flatten_xml(resp.content):
    ...
```
json from api:
```python
from iter_utils import flatten
import requests

resp = requests.get('url/to/api/endpoint')
for k, v in flatten(resp.json()):
    ...
```

You can find more by viewing the docstrings of the functions, including how the input and output looks like.

The functions flatten everything, including lists. Shortly there will be support for more convenient handling of lists along with options for pattern inference, html flattening, and more.