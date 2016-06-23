from imagescraper.items import Image
import datetime
import scrapy

class ImageSpider(scrapy.Spider):
    name = "image-spider"
    start_urls = ["https://www.reddit.com/r/pics"]
    img_extensions = ('.jpg', '.jpeg', '.png', '.gif')

    def parse(self, response):
        link_class = "\"thumbnail may-blank\""

        for url in response.css('a[class^=' + link_class + ']').xpath("@href").extract():
            if url.endswith(self.img_extensions):
                yield Image(file_urls=[url])
            else:
                yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
        for img_url in response.xpath("//img/@src").extract():
            if not (img_url.startswith("http")): 
                img_url = "https:" + img_url
            yield Image(file_urls=[img_url]) 
