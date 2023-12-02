import scrapy


class DocSpider(scrapy.Spider):
    name = "doc"
    allowed_domains = ["www.arzt-auskunft.de"]
    start_urls = ["https://www.arzt-auskunft.de/neurologie"]

    def parse(self, response):
        urls = response.xpath(
            "//div[@class='card dl mb-3']//a[@class='btn-detail']/@href")
        for url in urls:
            f_url = url.get()
            yield response.follow(f_url, callback=self.parse_doc)

        for i in range(2, 4):
            ur = f'https://www.arzt-auskunft.de/neurologie/{i}/'
            print(
                "##############################################################################")
            print(ur)
            yield response.follow(ur, callback=self.parse)

    def parse_doc(self, response):
        d_name = response.xpath('//h1/text()').get().split()

        f_name = ' '.join(d_name)
        r = response.url
        # address = response.xpath(
        #     "//div[@itemprop='address']/span/text()").get()
        # correct_address = [' '.join(add.splite()) for add in address]

        phone = response.xpath("//span[@itemprop='telephone']/a/text()").get()
        fax = response.xpath("//span[@itemprop='fax']/text()").get()
        yield {
            "name": f_name,
            # "address": correct_address,
            "phone": phone,
            "fax": fax,
            'url': r
        }
