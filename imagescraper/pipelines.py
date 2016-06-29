# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class ImagescraperPipeline(object):

    def __init__(self, postgres_uri, postgres_db):
        self.postgres_uri = postgres_uri
        self.postgres_db = postgres_db

    def process_item(self, item, spider):
        return item
