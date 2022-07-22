# Tokenizers
from typing import Any, List
from nltk.tokenize import (
    wordpunct_tokenize, sent_tokenize, word_tokenize, TweetTokenizer)
import spacy
from ekphrasis.classes.tokenizer import SocialTokenizer


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


class SpacyTokenizer:
    def __init__(self, pipline_model: str = "en_core_web_sm") -> None:
        self.nlp = spacy.load(pipline_model, disable=[
                              'ner', 'parser', 'lemmatizer'])

    def __call__(self, text: str) -> List[str]:
        return [token.text for token in self.nlp(text)]


class SocialTokenizer:
    def __init__(self) -> None:
        self.st = SocialTokenizer(lowercase=True)

    def __call__(self, text: str) -> List[str]:
        return self.st.tokenize(text)
