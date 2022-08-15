import pprint
import html

from NlpKickStart import (Pipeline, UnicodeNormalizer, EmojiHandler, RegexHandler, HashTagHandler, URLHandler,
                          HTMLHandler, MentionHandler, ReplaceHandler, PunctuationHandler, CaseFoldingNormalizer,
                          NLTKSentenceTokenizer, EmailHandler, ExpandContractionHandler)

sample_texts = [
    """They do this while filmed what do they do when they are not... we all know they murder! Defund the police 
    https://t.co/N1Vj0ACabb 😣 #BigMurder @CoderLone""",
    """"Saint Paul&#39;s fixes cancer 
    <br><a href=""https://jtvideos.blogspot.com/2022/05/saint-pauls-fixes-cancer.html""></a><br>
    During my PH D work at 
    Sheffield University 2000, we realised that ultrasound cause water to boil.  Welcome to molecular nuclear fusion.  
    For which professor Z refuses to take any credit.  Curious, an academic not waiting to take credit for the 
    students&#39; ideas. <br>1	H₂O+P+US→He+O+E #39;re doing biological molecular nuclear fusion. &amp;  The most 
    convenient type of physical molecular nuclear fusion is a lightening strike  Every 3 minutes around the world 
    there is a 1.5kmx2cm partial steam plasma. <br>	I became aware that ultrasound scans of cancers, 
    cause the emission of X rays.  Of which there is no chemical source!  You& <br>2	H₂O+P+TU→E²+L...Z-ray		
    here E²=2.5x10³⁰ W"	HxHnIZfuDGs""",
    'test test@gmail.com', "you're a big guy",
    "&quot;The task of literature is to reconnect us with feelings, which might otherwise be unbearable to "
    "study.&quot;&#39;",
    "FAVORITE LIKE FROM KUBRICK&#39;S FULL METAL JACKET:  &quot;YOU&#39;RE SO UGLY YOU COULD BE A MODERN ART "
    "MASTERPIECE!&quot;",
    "👍🙏", "Sir Lieutenant will be pronounced as लेफ्टिनेंट not ल्यूटिनेंट"]

pipeline = Pipeline([
    html.unescape,
    UnicodeNormalizer(),
    EmailHandler(),
    EmojiHandler(),
    RegexHandler("&#39;", "'"),
    ExpandContractionHandler(),
    HashTagHandler(keep=False),
    HTMLHandler(),
    URLHandler(keep=False),
    MentionHandler(keep=False),
    RegexHandler(r'\s+', ' '),
    RegexHandler(r"[^a-zA-Z0-9\. ]", ' '),
    CaseFoldingNormalizer(),
    RegexHandler(r"\.+", "."),
    RegexHandler(r"  +", " "),
    str.strip,
    NLTKSentenceTokenizer()
])

pprint.pprint(pipeline(sample_texts))
