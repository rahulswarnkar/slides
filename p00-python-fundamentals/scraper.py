from bs4 import BeautifulSoup
from requests import get
from contextlib import closing

def content(url):
    #TODO try catch
    with closing(get(url, stream=True)) as response:
        #TODO check for 200
        return response.content

def get_attrs(html, selector, attr):
    doc = BeautifulSoup(html, 'html.parser')
    elements = doc.select(selector)
    attrs = [element.attrs.get(attr) for element in elements]
    return attrs

def get_text(html, selector):
    doc = BeautifulSoup(html, 'html.parser')
    elements = doc.select(selector)
    texts = [element.text.strip() for element in elements]
    return texts
