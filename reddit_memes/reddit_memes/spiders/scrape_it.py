import scrapy


class ScrapeItSpider(scrapy.Spider):
    name = 'scrape_it'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def parse(self, response):
        pass
