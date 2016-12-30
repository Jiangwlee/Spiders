# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from newsmthimages.items import NewsmthimagesItem

class NewsmthSpider(Spider):
    name = 'newsmth'
    allowed_domains = ['newsmth.net']
    start_urls = ['http://newsmth.net/nForum/#!board/Picture']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_start_url, args={'wait': 0.5},)

    def parse_start_url(self, response):
        extractor = LxmlLinkExtractor(allow=r'http://newsmth.net/nForum/article/Picture/[0-9]+$')
        for link in extractor.extract_links(response):
            url = link.url + "?ajax&ajax"
            self.logger.info(url)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = NewsmthimagesItem()
        item['title'] = response.xpath('//title/text()').extract_first()
        self.logger.info("Title: %s" % item['title'])
        # get image_url
        for image_url in response.xpath('//img[@class="resizeable"]/@src').extract():
            if image_url.endswith('large'):
                image_url = image_url[:-6]
            self.logger.info(image_url)
        urlist = [url[:-6] for url in response.xpath('//img[@class="resizeable"]/@src').extract()]
        item['image_urls'] = urlist
        return item
