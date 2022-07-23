import emoji

from urlextract import URLExtract
import urllib


class EmojiHandler:
    def __call__(self, text: str) -> str:
        return emoji.demojize(text)


class URLHandler:
    def __init__(self, keep=True) -> None:
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
                text = text.replace(urls[i], ' ').strip()
            return text
