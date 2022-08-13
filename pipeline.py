from typing import List
from Normalizers import (
    UnicodeNormalizer, CaseFoldingNormalizer, RegexHandler)
from Tokenizers import (NLTKSentenceTokenizer, NLTKTweetTokenizer)
from Filterings import (EmojiHandler, HashTagHandler,
                        URLHandler, MentionHandler,
                        PunctuationHandler, ReplaceHandler,
                        HTMLHandler)
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
    sample_texts = ["""They do this while filmed what do they do when they are not... we all know they murder! Defund the police https://t.co/N1Vj0ACabb 😣 #BigMurder @CoderLone""",
                    """"Saint Paul&#39;s fixes cancer
                    <br><a href=""https://jtvideos.blogspot.com/2022/05/saint-pauls-fixes-cancer.html"">https://jtvideos.blogspot.com/2022/05/saint-pauls-fixes-cancer.html
                    </a><br>	During my PH D work at Sheffield University 2000, we realised that ultrasound cause water to boil.  Welcome to molecular nuclear fusion.  For which professor Z refuses to take any credit.  Curious, an academic not waiting to take credit for the students&#39; ideas.
                    <br>1	H₂O+P+US→He+O+E
                    #39;re doing biological molecular nuclear fusion. &amp;  The most convenient type of physical molecular nuclear fusion is a lightening strike  Every 3 minutes around the world there is a 1.5kmx2cm partial steam plasma.
                    <br>	I became aware that ultrasound scans of cancers, cause the emission of X rays.  Of which there is no chemical source!  You&
                    <br>2	H₂O+P+TU→E²+L...Z-ray		here E²=2.5x10³⁰ W"	HxHnIZfuDGs"""]

    pipeline = Pipeline([
        UnicodeNormalizer(),
        EmojiHandler(),
        RegexHandler("&#39;", "'"),
        HashTagHandler(keep=False),
        URLHandler(keep=False),
        HTMLHandler(),
        MentionHandler(keep=False),
        RegexHandler('\s+', ' '),
        ReplaceHandler(filters={'<br>': '', '&amp;': " and "}),
        PunctuationHandler(set(['.', "'"])),
        CaseFoldingNormalizer(),
        RegexHandler("\.+", "."),
        RegexHandler("  +", " "),
        NLTKSentenceTokenizer()

    ])

    pprint.pprint(pipeline(sample_texts))
