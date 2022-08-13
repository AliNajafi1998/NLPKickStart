from typing import Dict
import emoji
import string
from urlextract import URLExtract
import urllib
import re


class EmojiHandler:
    def __call__(self, text: str) -> str:
        return emoji.demojize(text)


class EmailHandler:
    def __init__(self, repl: str = ' ') -> None:
        self.pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
        self.repl = repl

    def __call__(self, text: str) -> str:
        match = re.findall(self.pattern, text)
        for m in match:
            text = text.replace(m, self.repl).strip()
        return text


class URLHandler:
    def __init__(self, keep: bool = True) -> None:
        self.url_extractor = URLExtract()
        self.keep = keep

    def __call__(self, text: str) -> str:
        urls = list(self.url_extractor.gen_urls(text))
        if self.keep == True:
            updated_urls = [
                url if 'http' in url else f'https://{url}' for url in urls]
            domains = [urllib.parse.urlparse(
                url_text).netloc for url_text in updated_urls]
            for i in range(len(domains)):
                text = text.replace(urls[i], domains[i])
            return text
        else:
            for i in range(len(urls)):
                text = text.replace(urls[i], '').strip()
            return text


class HashTagHandler:
    def __init__(self, keep: bool = True, do_camel_case_split: bool = True) -> None:
        self.keep = keep
        self.do_camel_case_split = do_camel_case_split

    def camel_case_split(self, text):
        pattern = '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)'
        matches = re.finditer(pattern, text)
        return " ".join([m.group(0) for m in matches])

    def __call__(self, text: str) -> str:
        pattern = r"(#([^\s]+))"
        if self.keep == True and self.do_camel_case_split == False:
            return re.sub(pattern, "\\1 \\2", text)
        elif self.keep == True and self.do_camel_case_split == True:
            return re.sub(pattern, lambda x: f"{x.group()} {self.camel_case_split(x.group()[1:])}", text)
        elif self.keep == False and self.do_camel_case_split == True:
            return re.sub(pattern, lambda x: f"{self.camel_case_split(x.group()[1:])}", text)
        else:
            return re.sub(pattern, "\\2", text)


class MentionHandler:
    def __init__(self, repl: str = None, keep: bool = True) -> None:
        self.repl = repl
        self.keep = keep

    def __call__(self, text: str) -> str:
        pattern = r"(@([^\s]+))"
        if self.repl:
            return re.sub(pattern, self.repl, text)
        else:
            if self.keep == True:
                return re.sub(pattern, "\\1 \\2", text)
            else:
                return re.sub(pattern, "\\2", text)


class PunctuationHandler:
    def __init__(self, keep_set: set = {}) -> None:
        self.punct_set = set(string.punctuation + '''…'"`’”“''' + '️')
        self.punct_set -= keep_set

    def __call__(self, text: str) -> str:
        cleaned_text = ""
        for ch in text:
            if ch not in self.punct_set:
                cleaned_text += ch
        return cleaned_text


class RegexHandler:
    def __init__(self, regex_pattern: str, repl: str = "", flags=0) -> None:
        self.regex_pattern = regex_pattern
        self.repl = repl
        self.flags = flags

    def __call__(self, text: str) -> str:
        return re.sub(self.regex_pattern, self.repl, text, flags=self.flags)


class ReplaceHandler:
    def __init__(self, filters: Dict[str, str]) -> None:
        self.filters = filters

    def __call__(self, text: str) -> str:
        output = text
        for k, v in self.filters.items():
            output = re.sub(k, v, output)
        return output


class HTMLHandler:
    def __call__(self, text: str) -> str:
        pattern = re.compile(r'<.*?>')
        return re.sub(pattern, " ", text)
