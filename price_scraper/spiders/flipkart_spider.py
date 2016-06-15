import scrapy
from price_scraper.items import PriceScraperItem


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = ['http://www.flipkart.com/search?q=moto+g3']

    def parse(self, response):
        div = response.xpath('//div[@class="gd-row browse-grid-row"]')[0]
        results = div.xpath('.//div[@class="gd-col gu3"]')
        for result in results:
            try:
                item = PriceScraperItem()
                item['name'] = result.xpath('.//a[@data-tracking-id="prd_title"]/@title').extract()[0]
                item['price'] = result.xpath('.//div[@class="pu-price"]')[0].xpath('.//span/text()').extract()[0]
                yield item
            except:
                pass
