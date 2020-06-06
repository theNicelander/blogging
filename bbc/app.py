from bs4 import BeautifulSoup as bs
import requests


class BBC:
    def __init__(self, url):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")

        self.body = self.get_body()
        self.title = self.get_title()

    def get_body(self):
        body = self.soup.find(property="articleBody")
        return [p.text for p in body.find_all("p")]

    def get_title(self):
        return self.soup.find(class_="story-body__h1").text
        