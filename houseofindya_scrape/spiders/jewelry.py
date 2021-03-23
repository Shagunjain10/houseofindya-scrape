import scrapy

class ListofNecklace(scrapy.Spider):
	name='list_of_necklace'
	start_urls = ['https://www.houseofindya.com/zyra/']

	def parse(self,response):
		description = response.xpath('//li//div[@class="catgName"]//p//text()').getall()
		pricelist = response.xpath('//li//div[@class="catgName"]//span//text()').getall()
		image_url = response.xpath('//li//div[@class="catgItem"]//img//@data-original').getall()

		for text,price,url in zip(description,pricelist,image_url):
			yield {
			'description':text,
			'price':price,
			'image_url':url
			}
