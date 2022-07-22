# Tokenizers
from typing import Any, List
from nltk.tokenize import (wordpunct_tokenize, sent_tokenize, word_tokenize)

class NLTKWordTokenizer:
    def __call__(self, text: str) -> List[str]:
        return word_tokenize(text)


class NLTKSentenceTokenizer:
    def __call__(self, text: str) -> List[str]:
        return sent_tokenize(text)


class NLTKWordPunctTokenizer:
    def __call__(self, text: str) -> List[str]:
        return wordpunct_tokenize(text)
