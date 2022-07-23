import unicodedata


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
