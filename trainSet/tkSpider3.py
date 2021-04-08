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
        with open('/Users/maciejkrzyszton/PycharmProjects/webscalper/webscalper/data2.json') as json_file:
            data = json.load(json_file)

            for p in data:
                request = Request(p['url'], cookies={'store_language': 'en'},callback=self.parse_article_page)
                print("yielding for url "+ p['url'])
                yield request

    def parse_article_page(self, response):
        tmp=''
        item=WebscalperItem()
        # Gets HTML content where the article links are stored

        header = response.xpath('//h1[@class="e-headline e-headline--h1 m-header__headline"]/text()').extract()
        #almost nice
        #body = response.xpath('//div[@class="g-faqantwort__answer-body"]'
        #                      '//p[@class="e-text"]/text()').extract()

        bodyExtra = response.xpath('//div[@class="g-faqantwort__answer-body"]'#)
                                   '//p[@class="e-text"]/text()').extract()




        for body_p in bodyExtra:#.xpath('//p[@class="e-text"]'):
            #print(body_p)
            tmp += ' '+ body_p


        #print("xpaths:")
        #print(header)
        print(bodyExtra)

        #for article_li in content.xpath('.//li'):
        #for article_a in content.xpath('.//a'):
        # Extracts the href info of the link to store in scrapy item
        item['header'] = header

        # for article_a in content.xpath('.//a'):
        item['body'] = tmp
        yield(item)
            #yield(Request(item.get('url'), cookies={'store_language': 'en'}, callback=self.parse_article_page))

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)