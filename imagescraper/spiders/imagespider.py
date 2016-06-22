from imagescraper.items import ImageScraper
import datetime
import scrapy

class ImageSpider(scrapy.Spider):
    name = "pyimagesearch-image-spider"
    start_urls = ["http://reddit.com/r/nba"]
    link_class = 'thumbnail may-blank'

    def parse(self, response):
        url = response.css().xpath("a[contains(., " + link_class + ")]")
        yield scrapy.Request(url.xpath("@href").extract_first(), self.parse_page)
