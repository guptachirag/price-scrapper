import scrapy
from price_scraper.items import PriceScraperItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=moto+g4+plus']
    handle_httpstatus_all = False

    def parse(self, response):
        ul = response.xpath('//ul[@id="s-results-list-atf"]')
        results = ul.xpath('.//li')[:4]
        for result in results:
            try:
                item = PriceScraperItem()
                item['name'] = result.xpath('.//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title').extract()[0]
                item['price'] = result.xpath('.//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract()[0]
                yield item
            except:
                pass
