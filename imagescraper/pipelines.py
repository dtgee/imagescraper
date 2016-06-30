# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

SETTINGS = get_project_settings()

class ImagescraperPipeline(object):

    def __init__(self):
        try:
            self.conn = psycopg2.connect('''
                                         db_name="{}",
                                         user="{}",
                                         password="{}",
                                         host="{}"
                                         '''.format(
                                                    SETTINGS['DB_NAME']
                                                    SETTINGS['DB_USER']
                                                    SETTINGS['DB_PASSWD']
                                                    SETTINGS['DB_HOST'])
        except:
            print "Unable to connect to database."

    def process_item(self, item, spider):
        cur = self.conn.cursor()

        try:
            cur.execute('''
                insert into image(path, url) values(%s, %s);
                ''', [
                item['image_urls'],
                item['images'][0]['path'],
                ])
        except:
            print "Failed to insert into database!"
            self.conn.commit()
            return item
