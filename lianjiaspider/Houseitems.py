# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	#标题
	title=scrapy.Field()
	#小区名
	name=scrapy.Field()
	#户型
	house_type=scrapy.Field()
	#面积
	area=scrapy.Field()
	#朝向
	orientation=scrapy.Field()
	#所在位置
	position=scrapy.Field()
	#房子楼层
	floor=scrapy.Field()
	#房子建筑时间
	build_time=scrapy.Field()
	#月租金
	monthly_rental=scrapy.Field()
	#更新时间
	update_time=scrapy.Field()
	#多少人看过
	visitors=scrapy.Field()
	#封面url
	image_url=scrapy.Field()
	#图片地址
	image_path=scrapy.Field()	
	#离地铁站距离
	to_subway=scrapy.Field()

