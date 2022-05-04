import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Homework5Spider(CrawlSpider):
    name = 'start'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='page-link']/@href"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='card']/a/@href"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//h3[@class='card-text']/text()").get()
        item['price'] = response.xpath("//h4/text()").get()
        item['image'] = response.xpath("//img[@class='card-img-top img-fluid']/@src").get()
        item['description'] = response.xpath("//p[@class='card-text']/text()").get()
        return item

