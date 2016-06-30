# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from scrapy.utils.project import get_project_settings

SETTINGS = get_project_settings()

class PostgresPipeline(object):

    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(database=SETTINGS['DB_NAME'],
                                         user=SETTINGS['DB_USER'],
                                         password=SETTINGS['DB_PASSWD'],
                                         host=SETTINGS['DB_HOST'])
        except:
            print "Unable to connect to database."

    def process_item(self, item, spider):
        cur = self.conn.cursor()

        try:
            cur.execute('''
                insert into images(path, url) values(%s, %s);
                ''', [
                item['image_urls'],
                item['images'][0]['path'],
                ])
        except:
            print "Failed to insert into database!"
            self.conn.commit()
            return item
