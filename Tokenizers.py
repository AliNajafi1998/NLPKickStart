# Tokenizers
from typing import Any, List
from nltk.tokenize import (
    wordpunct_tokenize, sent_tokenize, word_tokenize, TweetTokenizer)


class NLTKWordTokenizer:
    def __call__(self, text: str) -> List[str]:
        return word_tokenize(text)


class NLTKSentenceTokenizer:
    def __call__(self, text: str) -> List[str]:
        return sent_tokenize(text)


class NLTKWordPunctTokenizer:
    def __call__(self, text: str) -> List[str]:
        return wordpunct_tokenize(text)


class NLTKTweetTokenizer:
    def __init__(self) -> None:
        self.tt = TweetTokenizer()

    def __call__(self, text: str) -> List[str]:
        return self.tt.tokenize(text)