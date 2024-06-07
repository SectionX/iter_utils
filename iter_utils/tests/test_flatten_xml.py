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
    try:
        import xmltodict
    except:
        return

    xml_dict = xmltodict.parse(xml_string)
    results = []
    for k, _ in flatten(xml_dict):
        results.append(k)

    check = ['glossary.title', 'glossary.GlossDiv.title',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossTerm', 'glossary.GlossDiv.GlossList.GlossEntry.Acronym', 'glossary.GlossDiv.GlossList.GlossEntry.Abbrev',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossSee', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso']
    
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
    for a, b in zip(results, check):
        assert a == b