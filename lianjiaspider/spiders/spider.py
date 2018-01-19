#coding:utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from lianjiaspider.Houseitems import HouseItem

class Spider(scrapy.Spider):
	#爬虫名称
	name='lianjia'
	allowed_domains=['lianjia.com']
	page_link = set()
	start_urls=['https://gz.lianjia.com/zufang/']

	# for page in range(2,10):
	# 	url='https://gz.lianjia.com/zufang/pg'+str(page)
	# 	start_urls.append(url)

	def parse(self,response):
		item=HouseItem()
		for box in response.xpath('//ul[@class="house-lst"]/li'):
			item['title']=box.xpath('.//div[2]/h2/a/@title').extract()[0]
			item['name']=box.xpath('.//div[2]/div[1]/div[1]/a/span/text()').extract()[0]
			item['house_type']=box.xpath('.//div[2]/div[1]/div[1]/span[1]/span/text()').extract()[0]
			item['area']=box.xpath('.//div[2]/div[1]/div[1]/span[2]/text()').extract()[0]
			item['orientation']=box.xpath('.//div[2]/div[1]/div[1]/span[3]/text()').extract()[0]
			item['position']=box.xpath('.//div[2]/div[1]/div[2]/div/a/text()').extract()[0]
			item['floor']=box.xpath('.//div[2]/div[1]/div[2]/div').xpath('string(.)').extract()[0].split('/')[1]
			item['build_time']=box.xpath('.//div[2]/div[1]/div[2]/div').xpath('string(.)').extract()[0].split('/')[2]
			item['monthly_rental']=box.xpath('.//div[2]/div[2]/div[1]/span/text()').extract()[0]		
			item['update_time']=box.xpath('.//div[2]/div[2]/div[2]/text()').extract()[0]		
			item['visitors']=box.xpath('.//div[2]/div[3]/div[1]/div[1]/span/text()').extract()[0]	
			item['image_url']=box.xpath('.//div[1]/a/img/@data-img').extract()[0]
			try:	
				item['to_subway']=box.xpath('.//div[2]/div[1]/div[3]/div[1]/div[1]/span[@class="fang-subway-ex"]/span/text()').extract()[0]
			except:
				item['to_subway']=''
			yield item		

		#获取出租的房屋总数
		total_houses=int(response.xpath('//div[@class="list-head clear"]/h2/span/text()').extract()[0])
		for page in range(2,10):	
			url='https://gz.lianjia.com/zufang/pg'+str(page)
			yield scrapy.Request(url,callback=self.parse)	
