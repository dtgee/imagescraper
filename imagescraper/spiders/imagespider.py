from imagescraper.items import Image
import datetime
import scrapy
import urlparse

class ImageSpider(scrapy.Spider):
    name = "image-spider"
    start_urls = ["https://www.reddit.com/r/food"]
    img_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    xpath_extensions = '                            \
                          contains(., ".jpg")       \
                           or                       \
                          contains(., ".jpeg")      \
                           or                       \
                          contains(., ".png")       \
                           or                       \
                          contains(., ".gif")       \
                       '

    def parse(self, response):
        # Reddit labels its thumbnail class names with "thumbnail" "may-blank" amongst other classes
        data = response.xpath('//a[@class[contains(., "thumbnail") and contains(., "may-blank")]]/@href').extract()
        
        for url in data: 
            url = self.absolute_url(response, url)
            if any(ext in url for ext in self.img_extensions):
                yield Image(image_urls=[url])
            else:
                yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
        # Sometimes the links are to the images themselves rather than to a page that contains
        # images. If so, 'data' won't return anything useful and we would have an error using
        # response.xpath(), so we just grab the image url through response.url instead.
        try:
            data = response.xpath('//img                                   \
                                       [                                   \
                                         not(ancestor::a)                  \
                                       ]                                   \
                                    /@src                                  \
                                       [                                   \
                                         ' + self.xpath_extensions + '     \
                                       ]                                   \
                                   |                                       \
                                    //a                                    \
                                       [                                   \
                                         img/@src                          \
                                           [                               \
                                             ' + self.xpath_extensions + ' \
                                           ]                               \
                                       ]                                   \
                                    /@href                                 \
                                        [                                  \
                                          ' + self.xpath_extensions + '    \
                                        ]                                  \
                                  '                                        \
                                  )                                        \
                                  .extract()
            for img_url in data:
                img_url = self.absolute_url(response, img_url)
                yield Image(image_urls=[img_url]) 
        except AttributeError:
            if response.status == 200:
                yield Image(image_urls=[response.url])

    def absolute_url(self, response, url):
        url = urlparse.urljoin(response.url, url.strip())
        return url
