'''
Provides the PatternFinder class that attempts to find and count
all repeating patterns in a sequence of objects.
'''

from typing import Any, Generator, Callable, Iterable
from collections import Counter


class PatternFinder:
    '''
    Finds repeating patterns in a sequence. Depends on object equality
    so for custom classes make sure you define the __eq__ method.

    Does not guarantee order of insertion as it depends on collection.Counter
    class.
    '''

    def _fragment_sequence(self,
                           sequence: Iterable,
                           min_length: int
                           ) -> Generator[tuple[Any], None, None]:
        sequence = tuple(sequence)
        for step in range(min_length, len(sequence)):
            start_idx = 0
            end_idx = step
            while end_idx <= len(sequence):
                yield sequence[start_idx:end_idx]
                start_idx += 1
                end_idx += 1

    def iter_patterns(self, sequence: Iterable,
                      key: Callable | None = None, min_length: int = 1
                      ) -> Generator[tuple[tuple[Any], int], None, None]:
        '''
        find_all_patterns:
        Returns a Generator of all possible repeating patterns
        example:

        Input
        (4, 3, 2, 4, 3, 2, 3, 2)

        Output
        ((4, 3, 2), 2), ((4, 3), 2), ((3, 2), 3)
        '''
        _sequence: Iterable
        if key:
            _sequence = (key(item) for item in sequence)
        else:
            _sequence = sequence
        counter = Counter(self._fragment_sequence(_sequence, min_length))
        for k, v in counter.items():
            if v > 1:
                yield k, v

    def find_all_patterns(self, sequence: Iterable | Generator,
                          key: Callable | None = None, min_length: int = 1
                          ) -> Counter:
        '''
        find_all_patterns:
        Returns a Generator of all possible repeating patterns
        example:

        Input
        (4, 3, 2, 4, 3, 2, 3, 2)

        Output
        ((4, 3, 2), 2), ((4, 3), 2), ((3, 2), 3)
        '''

        _sequence: Iterable
        if key:
            _sequence = (key(item) for item in sequence)
        else:
            _sequence = sequence
        counter = Counter(self._fragment_sequence(_sequence, min_length))
        return counter

    # def find_b2b_patterns(self,
    #                       sequence: Sequence[Any], min_length: int = 2
    #                       ) -> Generator[tuple[tuple[Any], int], None, None]:
    #     '''
    #     find_b2b_patterns:
    #
    #     Returns a Generator of patterns that repeat sequentially
    #     example: (4, 3, 2, 4, 3, 2, 3, 2) -> ((4, 3, 2), 2), ((3, 2), 2)
    #     '''
    #     raise NotImplementedError
