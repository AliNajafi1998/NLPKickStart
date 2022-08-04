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
    def __call__(self, text: str, mode: str = 'lower') -> str:
        if mode == 'lower':
            return text.lower()
        elif mode == 'upper':
            return text.upper()
        else:
            raise Exception("Invalid mode!")


class NLTKStopwordHandler:
    def __init__(self, additional_stopwords: List[str]) -> None:
        nltk.download('stopwords')
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.stopwords.extend(additional_stopwords)

    def __call__(self, tokens: List[str]) -> str:
        return [token for token in tokens if token not in self.stopwords]


class NLTLPorterStemmer:
    def __init__(self) -> None:
        self.stemmer = PorterStemmer()

    def __call__(self, tokens: List[str]) -> str:
        return [self.stemmer.stem(token) for token in tokens]


class NLTKSNowBallStemmer:
    def __init__(self, language="english") -> None:
        self.stemmer = SnowballStemmer(language, ignore_stopwords=True)

    def __call__(self, tokens: List[str]) -> str:
        return [self.stemmer.stem(token) for token in tokens]


class NLTKWordNetLemmatizer:
    def __init__(self) -> None:
        self.lemmatizer = WordNetLemmatizer()

    def __call__(self, tokens: List[str]) -> str:
        return [self.lemmatizer.lemmatize(token) for token in tokens]
