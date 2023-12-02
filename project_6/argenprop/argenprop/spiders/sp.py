import scrapy


class SpSpider(scrapy.Spider):
    name = "sp"
    allowed_domains = ["www.argenprop.com"]
    start_urls = ["https://www.argenprop.com"]
    

    def parse(self, response):
        urls=response.xpath('(//h2[(text()="Propiedades en venta") or (text()="Propiedades en alquiler")])//..//a/@href')
        for url in urls:
            yield response.follow(url, callback=self.parse_result)
        
        # print(response.text)
#(//div[@class='suggested__search'][2]) 

    def parse_result(self,response):
        urls=response.xpath("//div[@class='listing__item ']/a/@href")
        for url in urls:
            
            yield response.follow(url, callback=self.parse_result_page)
        
        
        next_btn=response.xpath('//li[@class="pagination__page-next pagination__page"]')
        next_btn_url=response.xpath('//li[@class="pagination__page-next pagination__page"]/a/@href').get()
        
        if next_btn:
            yield response.follow(next_btn_url, callback=self.parse_result)
        
        
        
        


    def parse_result_page(self,response):
        titles=response.xpath('//h3[@class="titlebar__address"]/text()').get().strip()
        price=response.xpath('//p[@class="titlebar__price"]/text()').get().strip()
        yield{
            'title':titles,
            'price':price,
            }