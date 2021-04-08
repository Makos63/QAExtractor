import scrapy


class ArticlesscraperSpider(scrapy.Spider):
    name = 'ArticlesScraper'
    allowed_domains = ['https://www.tk.de/vertriebspartner/faq-2059618']
    start_urls = ['https://www.tk.de/vertriebspartner/faq/neuaufnahme-2059622',
                  'https://www.tk.de/vertriebspartner/faq/kuendigung-2063464',
                  'https://www.tk.de/vertriebspartner/faq/abrechnung-2063468',
                  'https://www.tk.de/vertriebspartner/faq/beitragsuebersicht-2063472',
                  'https://www.tk.de/vertriebspartner/faq/sonstige-2065472',
                  'https://www.tk.de/vertriebspartner/faq/wettbewerbsgrundsaetze-2063510']

    def parse(self, response):
        pass
