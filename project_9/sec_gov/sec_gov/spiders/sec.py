import scrapy
import urllib
#//a[contains(@href, 'pdf')]/@href
class SecSpider(scrapy.Spider):
    name = "sec"
    allowed_domains = ["www.sec.gov"]
    start_urls = ["https://www.sec.gov/spotlight/cybersecurity-enforcement-actions"]

    def parse(self, response):
        urls=response.xpath("//tr/td/a/@href")
        for url in urls:
            if "pdf" in url.get():
                yield {"pdf":url.get(),"url":response.url}
                
                ################# This code to download pdf  #############################
                # try:
                #     pdf_url = url.get()
                #     pdf_name = pdf_url.split("/")[-1]
                #     urllib.request.urlretrieve(pdf_url, pdf_name)
                # except:
                #     pass
                ################# This code to download pdf  #############################
                
            else:
                yield scrapy.Request(url=url.get(),method="GET",callback=self.parse_pdf)


    def parse_pdf(self,response):
        pdfs=response.xpath("//a[contains(@href, 'pdf')]/@href")
        if len(pdfs)==1:
            yield {"pdf":pdfs.get(),"url":response.url}
        else:
            for pdf in pdfs:
                yield {"pdf":pdf.get(),"url":response.url}    
