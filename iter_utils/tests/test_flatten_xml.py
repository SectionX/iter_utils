from iter_utils import flatten
from iter_utils import flatten_xml


xml_string = '''
<glossary><title>example glossary</title>
  <GlossDiv><title>S</title>
   <GlossList>
    <GlossEntry>
     <GlossTerm>Standard Generalized Markup Language</GlossTerm>
     <Acronym>SGML</Acronym>
     <Abbrev>ISO 8879:1986</Abbrev>
     <GlossDef>
      <para>A meta-markup language, used to create markup languages such as DocBook.</para>
      <GlossSeeAlso>GML</GlossSeeAlso>
      <GlossSeeAlso>XML</GlossSeeAlso>
     </GlossDef>
     <GlossSee>markup</GlossSee>
    </GlossEntry>
   </GlossList>
  </GlossDiv>
 </glossary>
'''

def test_flatten_using_xmltodict_library():
    import xmltodict

    xml_dict = xmltodict.parse(xml_string)
    results = []
    flattened = flatten(xml_dict)
    for k, _ in flattened:
        assert isinstance(_, str) or _ is None
        results.append(k)

    check = ['glossary.title', 'glossary.GlossDiv.title',
            'glossary.GlossDiv.GlossList.GlossEntry.GlossTerm', 'glossary.GlossDiv.GlossList.GlossEntry.Acronym', 'glossary.GlossDiv.GlossList.GlossEntry.Abbrev',
            'glossary.GlossDiv.GlossList.GlossEntry.GlossSee', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso',
            'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso']
    
    assert len(results) == flattened.length
    assert check == results


def test_flatten_using_flatten_xml():
    results = []
    flattened = flatten_xml(xml_string)
    for k, _ in flattened:
        results.append(k)

    check = ['glossary.title', 'glossary.GlossDiv.title',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossTerm', 'glossary.GlossDiv.GlossList.GlossEntry.Acronym', 'glossary.GlossDiv.GlossList.GlossEntry.Abbrev',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossSee', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso']
    
    assert len(results) == flattened.length
    assert results == check


def test_flatten_xml_init():
    import io
    from xml.etree.ElementTree import ElementTree

    strdoc = xml_string.strip()
    bytedoc = xml_string.encode()
    iodoc = io.BytesIO(bytedoc)
    etreedoc = ElementTree(file=io.BytesIO(bytedoc))

    assert isinstance(flatten_xml(strdoc)._doc, ElementTree)
    assert isinstance(flatten_xml(bytedoc)._doc, ElementTree)
    assert isinstance(flatten_xml(iodoc)._doc, ElementTree)
    assert isinstance(flatten_xml(etreedoc)._doc, ElementTree)
    try:
        flatten_xml({})._doc
    except Exception as e:
        assert isinstance(e, AttributeError)

def test_flatten_xml_update_namespace():
    flattened = flatten_xml(xml_string)
    assert flattened._update_namespace('', '.', 'rss') == 'rss'
    assert flattened._update_namespace('rss', '.', 'item') == 'rss.item'