from typing import List
from Normalizers import (
    UnicodeNormalizer, CaseFoldingNormalizer, RegexHandler)
from Tokenizers import (NLTKTweetTokenizer)
from Filterings import (EmojiHandler, HashTagHandler,
                        URLHandler, MentionHandler, PunctuationHandler)
import pprint


class Pipeline:
    def __init__(self, components: List) -> None:
        self.components = components

    def __call__(self, texts: List[str]) -> List[str]:
        outputs = []
        for text in texts:
            output = text
            for component in self.components:
                output = component(output)
            outputs.append(output)
        return outputs


if __name__ == '__main__':
    sample_texts = ["""They do this while filmed what do they do when they are not... we all know they murder! Defund the police https://t.co/N1Vj0ACabb 😣 #BigMurder @CoderLone"""]

    pipeline = Pipeline([
        UnicodeNormalizer(),
        EmojiHandler(),
        HashTagHandler(keep=False),
        URLHandler(keep=False),
        MentionHandler(keep=False),
        PunctuationHandler(set(['.'])),
        CaseFoldingNormalizer(),
        RegexHandler("\.+", "."),
        RegexHandler("  +", " "),
        NLTKTweetTokenizer()

    ])

    pprint.pprint(pipeline(sample_texts))
