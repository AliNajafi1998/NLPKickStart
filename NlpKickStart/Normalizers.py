import re
from typing import List

import unicodedata

import nltk
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer


class UnicodeNormalizer:
    def __init__(self) -> None:
        self.NFD = lambda text: unicodedata.normalize("NFD", text)
        self.NFKD = lambda text: unicodedata.normalize("NFKD", text)

    def __call__(self, text: str) -> str:
        return self.NFKD(self.NFD(text))


class CaseFoldingNormalizer:
    def __init__(self, mode: str = 'lower') -> None:
        self.mode = mode

    def __call__(self, text: str) -> str:
        if self.mode == 'lower':
            return text.lower()
        elif self.mode == 'upper':
            return text.upper()
        else:
            raise Exception("Invalid mode!")


class ExpandContractionHandler:
    def __call__(self, text: str) -> str:
        # specific
        text = re.sub(r"won\'t", "will not", text)
        text = re.sub(r"can\'t", "can not", text)
        text = re.sub(r"won\’t", "will not", text)
        text = re.sub(r"can\’t", "can not", text)

        text = re.sub(r"n\'t", " not", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'s", " is", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'t", " not", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'m", " am", text)

        text = re.sub(r"n\’t", " not", text)
        text = re.sub(r"\’re", " are", text)
        text = re.sub(r"\’s", " is", text)
        text = re.sub(r"\’d", " would", text)
        text = re.sub(r"\’ll", " will", text)
        text = re.sub(r"\’t", " not", text)
        text = re.sub(r"\’ve", " have", text)
        text = re.sub(r"\’m", " am", text)

        return text


class NLTKStopwordHandler:
    def __init__(self, additional_stopwords: List[str]) -> None:
        nltk.download('stopwords')
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.stopwords.extend(additional_stopwords)

    def __call__(self, tokens: List[str]) -> list[str]:
        return [token for token in tokens if token not in self.stopwords]


class NLTLPorterStemmer:
    def __init__(self) -> None:
        self.stemmer = PorterStemmer()

    def __call__(self, tokens: List[str]) -> list[str]:
        return [self.stemmer.stem(token) for token in tokens]


class NLTKSNowBallStemmer:
    def __init__(self, language="english") -> None:
        self.stemmer = SnowballStemmer(language, ignore_stopwords=True)

    def __call__(self, tokens: List[str]) -> list[str]:
        return [self.stemmer.stem(token) for token in tokens]


class NLTKWordNetLemmatizer:
    def __init__(self) -> None:
        self.lemmatizer = WordNetLemmatizer()

    def __call__(self, tokens: List[str]) -> list[str]:
        return [self.lemmatizer.lemmatize(token) for token in tokens]
