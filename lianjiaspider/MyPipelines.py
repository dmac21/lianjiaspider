# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import io,json

class MyPipeline(object):
	def __init__(self):
		self.file=io.open('data.json','w',encoding='utf-8')

	def process_item(self, item, spider):
		line=json.dumps(dict(item),ensure_ascii=False)+'\n'
		self.file.write(line)
		return item

	def open_spider(self,spider):
		pass

	def close_spider(self,spider):
		pass      

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import copy
class MySQLStorePipeline(object):
    #数据库参数
    def __init__(self):
        dbargs = dict(
             host = '127.0.0.1',
             db = 'test',
             user = 'root',
             passwd = '',
             cursorclass = MySQLdb.cursors.DictCursor,
             charset = 'utf8',
             use_unicode = True
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
    	asynItem = copy.deepcopy(item) 
    	res = self.dbpool.runInteraction(self.insert_into_table,asynItem)
        return item
    #插入的表，此表需要事先建好
    def insert_into_table(self,conn,item):
            conn.execute('insert into lianjia_data(title, name, house_type,area,orientation,position,floor,build_time,monthly_rental,update_time,visitors,image_url,to_subway) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
				item['title'],
				item['name'],
				item['house_type'],
				item['area'],
				item['orientation'],
				item['position'],
				item['floor'],
				item['build_time'],
				item['monthly_rental'],	
				item['update_time'],
				item['visitors'],
				item['image_url'],
				item['to_subway'])
                )    