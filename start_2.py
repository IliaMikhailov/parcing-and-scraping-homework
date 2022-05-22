import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest

class Homework6Spider(CrawlSpider):
    name = 'start'
    allowed_domains = ['scrapingclub.com']
    start_urls = []
    script = '''
        function main(splash,args)
            url = args.url
            assert(splash:go(url)
            assert(splash:wait(1))
            return splash:html()
            end
    '''

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//h4[@class='card-title']/text()").get()
        item['price'] = response.xpath("//h4[@class='card-price']/text()").get()
        item['image'] = response.xpath("//img[@class='card-img-top img-fluid']/@src").get()
        item['description'] = response.xpath("//p[@class='card-description']/text()").get()
        return item

    def start_requests(self):
        yield  SplashRequest{
            url = 'https://scrapingclub.com/exercise/detail_sign/js',
            callback = self.parse_item(),
            endpoint = 'execute',
            args = {
                'lua_source':self.script
                }
        }
