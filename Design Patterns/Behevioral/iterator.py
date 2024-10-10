#Iterator Pattern

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class SecuencialIterartor(Iterator):

    def __init__(self, collection: NumberCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> Any:
        if self._position < 0 or self._position >= len(self._collection):
            raise StopIteration()
         
        value = self._collection[self._position]
        self._position += -1 if self._reverse else 1
        return value
    
    def has_next(self) -> bool:
        return 0 <= self._position < len(self._collection)
    

class NumberCollection(Iterable):

    def __init__(self) -> None:
        self._numbers = []

    def add_number(self, number:int) -> None:
        self._numbers.append(number)

    def __getitem__(self, index: int) -> int:
        return self._numbers[index]
    
    def __iter__(self) -> SecuencialIterartor:
        return SecuencialIterartor(self)

    def get_reverse_iterator(self) -> SecuencialIterartor:
        return SecuencialIterartor(self, True)

    def __len__(self) -> int:
        return len(self._numbers)
    


if __name__ == "__main__":

    number_collection = NumberCollection()
    number_collection.add_number(10)
    number_collection.add_number(20)
    number_collection.add_number(30)
    
    print("Ascending Order:")
    ascending_iterator = number_collection.__iter__()
    while ascending_iterator.has_next():
        print(ascending_iterator.__next__())

    print("\nDescending Order:")
    reverse_iterator = number_collection.get_reverse_iterator()
    while reverse_iterator.has_next():
        print(reverse_iterator.__next__())