# WebScraper

### Create Virtual Environment (optional)
Shell:
```
python3 -m venv scraper
source ./bin/activate
```

### Dependencies
We will use [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) for parsing HTML and [requests](https://pypi.org/project/requests/) for fetching web pages.

Shell:
```
pip3 install BeautifulSoup4 requests
```

## Parse HTML

Create a simple HTML file with the following content. Let's call it `simple.html`.
```
<!DOCTYPE html>
<html>
<head>
  <title>Simple Page</title>
</head>
<body>
  <h3>Python is fun!</h3>
  <p id="yes">Yes it is!!</p>
  <p class="hyperlink">
    <a href="https://www.python.org/">Get it here...</a>
  </p>
</body>
</html>
```
Let's read it in REPL:
```
>>> from contextlib import closing
>>> from bs4 import BeautifulSoup

>>> with closing(open('simple.html')) as file:
...   html = file.read()
...   print(html)
...

>>> doc = BeautifulSoup(html, 'html.parser')
```

Now that the document is loaded, we can look for different nodes within the HTML DOM.

Try the following in REPL:
```
>>> doc.find('p')

>>> doc.select('#yes)

>>> doc.select_one('#yes).text

>>> doc.find_one('a').attrs
```

## Fetch a webpage
Import the modules.

REPL:
```
>>> from requests import get
>>> from contextlib import closing
```
Define url and fetch content of the page.

REPL:
```
>>> url = 'https://www.hermes.com/uk/en/product/izmir-sandal-H101203ZH32420/'
>>> with closing(get(url, stream=True)) as response:
...    content = response.content
...    print(content)
```
### Inspect the page
Open the same page in a browser and inspect the DOM.

Look for the label and price field and try to identify the element name, classes or id that can identify them.
REPL:
```
>>> html = BeautifulSoup(content, 'html.parser')
>>> html.select('p.field-type-commerce-price')

>>> html.select('p.field-type-commerce-price').text

>>> html.select('p.field-type-commerce-price').text.strip()

```