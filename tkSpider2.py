import scrapy
from scrapy.http import Request
from webscalper.items import WebscalperItem
import json

class ArticlesSpider(scrapy.Spider):
    name = 'ArticlesScraper'
    allowed_domains = ['www.tk.de']


    def __init(self):
        self.extractedUrlList = []
        self.visitedURLs = set()
        self.unvisitedURLs = set()

    def start_requests(self):
        with open('/Users/maciejkrzyszton/PycharmProjects/webscalper/webscalper/data-eval.json') as json_file:
            data = json.load(json_file)

            for p in data:
                request = Request(p['url'], cookies={'store_language': 'en'},callback=self.parse_article_page)
                print("yielding for url "+ p['url'])
                yield request

    def parse_article_page(self,response):
        item=WebscalperItem()
        # Gets HTML content where the article links are stored
        #content=response.xpath('//div[@class="t-faq"]'
        #                       '//div[@class="m-verteilerliste"]'
        #                       '//div[@class="m-verteilerliste__link-container"]')
        content = response.xpath(#'//main[@class="u-viewport"]'
                                 #'//div[@class="t-faq "]'
                                 '//section[@class="c-artikelliste "]')
                                 #'//div[@class="m-verteilerliste m-verteilerliste--questionlist m-verteilerliste--1columns m-verteilerliste--icon is-loaded is-active"]')
                                 #'//nav[@class="m-verteilerliste__container"]'
                                 #'//ul[@class="m-verteilerliste__links "]')


        # Loops through the each and every article link in HTML 'content'
        print("content.xpath:")
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