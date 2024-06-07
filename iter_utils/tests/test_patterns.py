from iter_utils import PatternFinder

input_simple = (4, 3, 2, 4, 3, 2, 3, 2)
output_simple = ((4, 3, 2), 2), ((4, 3), 2), ((3, 2), 3)

input_complex = ((4, ), (3, ), (2, ), (4, ), (3, ), (2, ), (3, ), (2, ))
output_complex = ((4, 3, 2), 2), ((4, 3), 2), ((3, 2), 3)


def test_simple_PatternFinder():
    pf = PatternFinder()
    patterns = tuple(pf.iter_patterns(input_simple, min_length=2))
    assert set(patterns) == set(output_simple)

    result = []
    for k, v in pf.find_all_patterns(input_simple, min_length=2).items():
        if v >= 2:
            result.append((k, v))
    assert set(result) == set(output_simple)

def test_complex_PatternFinder():
    pf = PatternFinder()
    patterns = tuple(pf.iter_patterns(input_complex, min_length=2, key = lambda x: x[0]))
    assert set(patterns) == set(output_complex)

    result = []
    for k, v in pf.find_all_patterns(input_complex, min_length=2, key = lambda x: x[0]).items():
        if v >= 2:
            result.append((k, v))
    assert set(result) == set(output_simple)


