import scrapy
from scrapy.http import Request
from webscalper.items import WebscalperItem
import time

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['www.tk.de']
    start_urls = ['https://www.tk.de/vertriebspartner/faq/neuaufnahme-2059622',
                  'https://www.tk.de/vertriebspartner/faq/kuendigung-2063464',
                  'https://www.tk.de/vertriebspartner/faq/abrechnung-2063468',
                  'https://www.tk.de/vertriebspartner/faq/beitragsuebersicht-2063472',
                  'https://www.tk.de/vertriebspartner/faq/sonstige-2065472',
                  'https://www.tk.de/vertriebspartner/faq/wettbewerbsgrundsaetze-2063510']

    def __init(self):
        self.extractedUrlList = []
        self.visitedURLs = set()
        self.unvisitedURLs = set()

    def start_requests(self):
        r=Request('https://www.tk.de/vertriebspartner/faq/neuaufnahme-2059622', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield(r)
        r = Request('https://www.tk.de/vertriebspartner/faq/kuendigung-2063464', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield (r)
        r = Request('https://www.tk.de/vertriebspartner/faq/abrechnung-2063468', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield (r)
        r = Request('https://www.tk.de/vertriebspartner/faq/beitragsuebersicht-2063472', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield(r)
        r = Request('https://www.tk.de/vertriebspartner/faq/sonstige-2065472', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield(r)
        r = Request('https://www.tk.de/vertriebspartner/faq/wettbewerbsgrundsaetze-2063510', cookies={'store_language': 'en'}, callback=self.parse_article_page)
        yield(r)
        #time.sleep(1)

    def parse_article_page(self,response):
        item=WebscalperItem()
        # Gets HTML content where the article links are stored
        #content=response.xpath('//div[@class="t-faq"]'
        #                       '//div[@class="m-verteilerliste"]'
        #                       '//div[@class="m-verteilerliste__link-container"]')
        content = response.xpath(#'//main[@class="u-viewport"]'
                                 #'//div[@class="t-faq "]'
                                 '//section[@class="c-navigationsliste "]')
                                 #'//div[@class="m-verteilerliste m-verteilerliste--questionlist m-verteilerliste--1columns m-verteilerliste--icon is-loaded is-active"]')
                                 #'//nav[@class="m-verteilerliste__container"]'
                                 #'//ul[@class="m-verteilerliste__links "]')


        # Loops through the each and every article link in HTML 'content'
        print("current site")
        print(item.get('url'))
        print("content.xpath")
        print(content)

        #for article_li in content.xpath('.//li'):
        for article_a in content.xpath('.//a'):
            # Extracts the href info of the link to store in scrapy item
            item['url'] = article_a.xpath('.//@href').extract_first()
            item['url'] = "https://www.tk.de"+item['url']
            yield(item)
            #yield(Request(item.get('url'), cookies={'store_language': 'en'}, callback=self.parse_article_page))

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)