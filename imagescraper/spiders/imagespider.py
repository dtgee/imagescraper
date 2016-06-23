from imagescraper.items import Image
import datetime
import scrapy

class ImageSpider(scrapy.Spider):
    name = "pyimagesearch-image-spider"
    start_urls = ["https://www.reddit.com/r/pics"]
    link_class = "thumbnail may-blank"

    def parse(self, response):
        for url in response.css('a[class^=' + link_class + ']').xpath("@href").extract():
        # TODO: grab image if it is already an image
        # "Click" url if it is not an image
            yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
        img_url = response.xpath("//img/@src").extract()
        
        yield Image(file_urls=[img_url]) 
