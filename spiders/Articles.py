import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['https://www.tk.de/vertriebspartner/faq-2059618']
    start_urls = ['http://https://www.tk.de/vertriebspartner/faq-2059618']

    def parse(self, response):
        pass
