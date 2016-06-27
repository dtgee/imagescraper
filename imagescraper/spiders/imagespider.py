from imagescraper.items import Image
import datetime
import scrapy
import urlparse

class ImageSpider(scrapy.Spider):
    name = "image-spider"
    start_urls = ["https://www.reddit.com/r/pics"]
    img_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    handle_httpstatus_list = [301, 302]
    handle_httpstatus_all = False

    def parse(self, response):
        link_class = "\"thumbnail may-blank\""

        for url in response.css('a[class^=' + link_class + ']').xpath("@href").extract():
            url = self.absolute_url(response, url)
            # change to if url contains .jpeg
            if url.endswith(self.img_extensions):
                yield Image(file_urls=[url])
            else:
                yield scrapy.Request(url, self.parse_page)

    def parse_page(self, response):
#//img[not(ancestor::a)]/@src[contains(., ".jpg")] | //a[img/@src[contains(., ".jpg")]]/@href
        try:
            data = response.xpath('//img                                \
                                          [                             \
                                            not(ancestor::a)            \
                                          ]                             \
                                       /@src                            \
                                        [                               \
                                            contains(., ".jpg")         \
                                             or                         \
                                            contains(., ".jpeg")        \
                                             or                         \
                                            contains(., ".png")         \
                                             or                         \
                                            contains(., ".gif")         \
                                        ]                               \
                                      |                                 \
                                       //a                              \
                                        [                               \
                                            img/@src                    \
                                            [                           \
                                                 contains(., ".jpg")    \
                                                  or                    \
                                                 contains(., ".jpeg")   \
                                                  or                    \
                                                 contains(., ".png")    \
                                                  or                    \
                                                 contains(., ".gif")    \
                                            ]                           \
                                        ]                               \
                                       /@href                           \
                                      '                                 \
                                     )                                  \
                                     .extract()
            for img_url in data:
                img_url = self.absolute_url(response, img_url)
                yield Image(file_urls=[img_url]) 
        except AttributeError:
            if response.status == 200:
                yield Image(file_urls=[response.url])

    def absolute_url(self, response, url):
        url = urlparse.urljoin(response.url, url.strip())
        return url
