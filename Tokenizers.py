from typing import List

import spacy
from ekphrasis.classes.tokenizer import SocialTokenizer
from nltk.tokenize import (wordpunct_tokenize, sent_tokenize,
                           word_tokenize, TweetTokenizer)


class NLTKWordTokenizer:
    def __init__(self) -> None:
        pass

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


class SpacySentenceTokenizer:
    def __init__(self, pipline_model: str = "en_core_web_sm") -> None:
        self.nlp = spacy.load(pipline_model)

    def __call__(self, text: str) -> List[str]:
        return list(self.nlp(text).sents)


class SocialMediaTokenizer:
    def __init__(self, lowercase: bool = True) -> None:
        self.st = SocialTokenizer(lowercase=lowercase)

    def __call__(self, text: str) -> List[str]:
        return self.st.tokenize(text)
