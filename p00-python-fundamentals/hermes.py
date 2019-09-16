import scraper

def collect_urls(products_url, prefix = ''):
    products_html = scraper.content(products_url)
    products_hrefs = scraper.get_attrs(products_html, 'div.product-item a', 'href')
    product_urls = [(prefix + href) for href in products_hrefs]
    return product_urls

def collect_info(product_url):
    product_html = scraper.content(product_url)
    info = {
        'name': scraper.get_text(product_html, 'div#variant-info h1').pop(),
        'sku': scraper.get_text(product_html, 'div.commerce-product-sku span').pop(),
        'price': scraper.get_text(product_html, 'p.field-type-commerce-price').pop()
    }
    return info

urls = collect_urls('https://www.hermes.com/uk/en/men/shoes/', 'https://www.hermes.com/')
for url in urls:
    print(collect_info(url))