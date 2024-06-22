from .base import BaseTools
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebTools(BaseTools):
    register_default = ['get_all_links', 'get_content']
    def __init__(self, register=[]):
        super().__init__(register, self.register_default)

    def get_all_links(self, url):
        """Retrieve all links from a given URL and return a list of tuples containing the link text and the absolute URL"""
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page: {url}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")

        links = [
            (a.text, urljoin(url, a["href"]))
            for a in soup.find_all("a", href=True)
            if a["href"]
        ]

        return links

    def get_content(self, url):
        """Retrieve the text content from a given URL and return it as a string"""
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page: {url}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        text_content = soup.get_text()

        return text_content

import os
from exa_py import Exa
from .base import BaseTools

class ExaTools(BaseTools):
    register_default = ['search', 'find_similar', 'get_contents']

    def __init__(self, register=[]):
        super().__init__(register, self.register_default)
        self.exa = Exa(api_key=os.environ["EXA_API_KEY"])

    def search(self, query: str):
        """Search for a webpage based on the query."""
        return self.exa.search(f"{query}", use_autoprompt=True, num_results=5)

    def find_similar(self, url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return self.exa.find_similar(url, num_results=5)

    def get_contents(self, ids: list[str]):
        """Get the contents of a webpage.
        The ids passed in should be a list of ids returned from `search`.
        """
        return self.exa.get_contents(ids)

