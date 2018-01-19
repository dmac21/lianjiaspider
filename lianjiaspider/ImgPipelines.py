# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
	def get_media_requests(self,item,info):
		yield scrapy.Request(item['image_url'])

	def item_completed(self,result,item,info,):
		image_path=[x['path'] for ok,x in result if ok ]
		if not image_path:
			raise DropItem("Item contains no images")
		item['image_path'] = image_path
		return item	
