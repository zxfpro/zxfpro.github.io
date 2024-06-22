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
