import scrapy

class MySpider(scrapy.Spider):
    name = 'tx'

    def start_requests(self):
        url = "https://www.tax.service.gov.uk/check-register-fair-rents/search"
        payload = {'csrfToken':'88f52d895d412e742e5951abfa626a13bb6b3711-1698776780452-760755e97cca78d06f6cadb4',
                "q":'da1',
                }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.tax.service.gov.uk/check-register-fair-rents/search?_ga=2.174123170.1467572594.1698776620-714798677.1698776620',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.tax.service.gov.uk',
            'Connection': 'keep-alive',
            'Cookie': 'mdtpdi=mdtpdi#4f7cc70d-0f31-4eab-93d4-6f10a0da5915#1698775269283_QqGqS8+kHCD0c/cER+Y81Q==; mdtp=UHpHHmQG0mPAJQEahKmWVY7re5pXkynmuzpberXaq4uqOaP+gmoFCeG3XEcIQrDvLQMTqr69MaIgDQffBugv6/7+yTM5o+cRvNjcvh05ISIj40pAYkTkOWsAFaQIRwy7ltm1FH9qrXN4SfeikHAQs6FmMaR0mjB5z0GPlOV4PMf7GKDmXeIlZJ7t7aIwDStMyL5grc8S1WFQNJtIarqAqZLenNqOHH7sLfNCIBVhAuDqQJnaYM2/xIZhFD2kEefOO+FgIEfbbIAWEgoRFSvvbYw7jFB/CJl2KIrWakpKNf8BPZvQmVHGLu27; userConsent={%22version%22:%222021.1%22%2C%22datetimeSet%22:%222023-10-31T18:01:13.248Z%22%2C%22preferences%22:{%22measurement%22:true%2C%22settings%22:true}}; _ga_Y4LWMWY6WS=GS1.5.1698775273.1.1.1698776781.0.0.0; _ga=GA1.5.376439445.1698775274; _ga_Y4LWMWY6WS=GS1.1.1698775273.1.1.1698775290.0.0.0; _ga=GA1.4.714798677.1698776620; _gid=GA1.4.1467572594.1698776620; _gat_UA-43414424-1=1; mdtp=VjV/iIflvoweL2Q0LnncvVQATrNCJZNMiysZ3V+aCSXiqWWD61DLvscKi8N98fPtfqlzV2Ndk2q+FBTKkEiGMqczjYu8BHnv4lV0I6jKDsN3TI6m9pAxDatexCXexDlGmOz42v//Z5VDmzz1CzxREg8k/eboCkfGTFCG1pgv6/jaW8gvmjvP9TVSpTtKNDp/NBXlPQ5MqFuYW0BDmae81qxP5mpVuSCTuUIRIp3mNDHQxvm0hMR5iyQJcXh3QISjm6bJaKYPjsBmXv92nRLl6BhUEfCbtSxiTaV6kYxnxUCkOD4o2cxk9aHH; mdtpdi=mdtpdi#4f7cc70d-0f31-4eab-93d4-6f10a0da5915#1698775269283_QqGqS8+kHCD0c/cER+Y81Q==',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers'
        }

        yield scrapy.FormRequest(url=url, method='POST', formdata=payload, headers=headers, callback=self.parse)

    def parse(self, response):
        urls=response.xpath('//tr//td/a/@href')
        
        
        
        for url in urls:
            print(url.get())
            yield response.follow(url, callback=self.parse_result)

        next_btn=response.xpath("//ul[@class='govuk-list pagination']/li/a[@aria-label='Next page']/@href").get()
        # for i in range(2):
        if next_btn is not None:
            ur='https://www.tax.service.gov.uk'+ next_btn
            yield response.follow(ur, callback=self.parse)
        
#         # print(next_btn)
        
    
    def parse_result(self,response):

        address = response.xpath("//h1/text()")
        price = response.xpath("//dd[@class='govuk-summary-list__value']/text()")

        print("#"*100)
        # print(name)
        # print(len(name))
        yield{
            "address":address.get().strip(),
            "price":price.get().strip()
        }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# import scrapy

# class MySpider(scrapy.Spider):
#     name = 'tx'

#     def start_requests(self):
#         url = "https://www.tax.service.gov.uk/check-register-fair-rents/search"
#         payload = {'csrfToken':'88f52d895d412e742e5951abfa626a13bb6b3711-1698776780452-760755e97cca78d06f6cadb4',
#                 "q":'da1',
#                 }
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Referer': 'https://www.tax.service.gov.uk/check-register-fair-rents/search?_ga=2.174123170.1467572594.1698776620-714798677.1698776620',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Origin': 'https://www.tax.service.gov.uk',
#             'Connection': 'keep-alive',
#             'Cookie': 'mdtpdi=mdtpdi#4f7cc70d-0f31-4eab-93d4-6f10a0da5915#1698775269283_QqGqS8+kHCD0c/cER+Y81Q==; mdtp=UHpHHmQG0mPAJQEahKmWVY7re5pXkynmuzpberXaq4uqOaP+gmoFCeG3XEcIQrDvLQMTqr69MaIgDQffBugv6/7+yTM5o+cRvNjcvh05ISIj40pAYkTkOWsAFaQIRwy7ltm1FH9qrXN4SfeikHAQs6FmMaR0mjB5z0GPlOV4PMf7GKDmXeIlZJ7t7aIwDStMyL5grc8S1WFQNJtIarqAqZLenNqOHH7sLfNCIBVhAuDqQJnaYM2/xIZhFD2kEefOO+FgIEfbbIAWEgoRFSvvbYw7jFB/CJl2KIrWakpKNf8BPZvQmVHGLu27; userConsent={%22version%22:%222021.1%22%2C%22datetimeSet%22:%222023-10-31T18:01:13.248Z%22%2C%22preferences%22:{%22measurement%22:true%2C%22settings%22:true}}; _ga_Y4LWMWY6WS=GS1.5.1698775273.1.1.1698776781.0.0.0; _ga=GA1.5.376439445.1698775274; _ga_Y4LWMWY6WS=GS1.1.1698775273.1.1.1698775290.0.0.0; _ga=GA1.4.714798677.1698776620; _gid=GA1.4.1467572594.1698776620; _gat_UA-43414424-1=1; mdtp=VjV/iIflvoweL2Q0LnncvVQATrNCJZNMiysZ3V+aCSXiqWWD61DLvscKi8N98fPtfqlzV2Ndk2q+FBTKkEiGMqczjYu8BHnv4lV0I6jKDsN3TI6m9pAxDatexCXexDlGmOz42v//Z5VDmzz1CzxREg8k/eboCkfGTFCG1pgv6/jaW8gvmjvP9TVSpTtKNDp/NBXlPQ5MqFuYW0BDmae81qxP5mpVuSCTuUIRIp3mNDHQxvm0hMR5iyQJcXh3QISjm6bJaKYPjsBmXv92nRLl6BhUEfCbtSxiTaV6kYxnxUCkOD4o2cxk9aHH; mdtpdi=mdtpdi#4f7cc70d-0f31-4eab-93d4-6f10a0da5915#1698775269283_QqGqS8+kHCD0c/cER+Y81Q==',
#             'Upgrade-Insecure-Requests': '1',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-User': '?1',
#             'TE': 'trailers'
#         }

#         yield scrapy.FormRequest(url=url, method='POST', formdata=payload, headers=headers, callback=self.parse)


#     def parse(self, response):
        
#         results = response.xpath("//table/tbody/tr")
#         for result in results:
#             relative_url = result.xpath(".//td/a/@href").get()
#             url = "https://www.tax.service.gov.uk" + relative_url
#             print("#"*100)
#             print(url)
            
#             yield response.follow(url, callback=self.parse_result)

#         next_page= response.xpath("//ul[@class='govuk-list pagination']/li/a[@aria-label='Next page']/@href").get()
#         if next_page is not None:
#             next_page_url = "https://www.tax.service.gov.uk" + next_page 
#             # print("#"*100)
#             # print(next_page_url)
#             yield response.follow(next_page_url, callback=self.parse)


#     def parse_result(self,response):

#         address = response.xpath("//h1/text()")
#         price = response.xpath("//dd[@class='govuk-summary-list__value']/text()")

#         print("#"*100)
#         # print(name)
#         # print(len(name))
#         yield{
#             "address":address.get().strip(),
#             "price":price.get().strip()
#         }