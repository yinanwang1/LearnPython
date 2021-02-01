from typing import List
from collections import Counter

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.counter = dict(Counter(book))

    def get(self, word: str) -> int:
        return self.counter.get(word, None)