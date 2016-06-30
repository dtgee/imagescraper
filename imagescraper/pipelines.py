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
            self.conn.autocommit = True
        except Exception,e:
            print "Unable to connect to database."
            print str(e)

    def process_item(self, item, spider):
        if item['images']:
            cur = self.conn.cursor()
            SQL = "insert into images(path, url)
                    select
                        (%s, %s)
                    where not exists (
                        select * from images where path = %s and url = %s
                    );"
            SQL_data = (item['images'][0]['path'], item['image_urls'][0]) 
            try:
                cur.execute(SQL, SQL_data)
            except Exception,e:
                print "Failed to insert into database!"
                print str(e)
        return item
