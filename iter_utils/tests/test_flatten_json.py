from iter_utils import flatten
import json

json_string = '''
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossSee": "markup",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    }
                }
            }
        }
    }
}
'''

def test_flatten_json():
    json_dict = json.loads(json_string)
    results = []
    for k, _ in flatten(json_dict):
        results.append(k)

    check = ['glossary.title', 'glossary.GlossDiv.title', 'glossary.GlossDiv.GlossList.GlossEntry.ID', 'glossary.GlossDiv.GlossList.GlossEntry.SortAs',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossTerm', 'glossary.GlossDiv.GlossList.GlossEntry.Acronym', 'glossary.GlossDiv.GlossList.GlossEntry.Abbrev',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossSee', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para', 'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso',
             'glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso']
    assert results == check


