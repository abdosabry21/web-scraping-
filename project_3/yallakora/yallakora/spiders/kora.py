import scrapy


class KoraSpider(scrapy.Spider):
    date = "10/20/2023"
    name = "kora"
    allowed_domains = ["www.yallakora.com"]
    start_urls = [
        f"https://www.yallakora.com/match-center?date={date}#days"]

    def parse(self, response):
        matchs_url = response.xpath(
            "//div[@class='leftCol']/a/@href")

        for i in matchs_url:

            new_url = i.get()
            print("####################################")
            print(new_url)
            yield response.follow(new_url, callback=self.parse_match)

    def parse_match(self, response):
        try:
            champ = response.xpath(
                "//div[@class='tourNameBtn']/a[1]/text()").get()

            teamA = response.xpath(
                "//div[@class='team teamA']//p/text()").get()

            teamB = response.xpath(
                "//div[@class='team teamB']//p/text()").get()

            teamAR = response.xpath(
                "(//div[@class='result']/span[1]/text())[1]").get()
            teamBR = response.xpath(
                "(//div[@class='result']/span[2]/text())[1]").get()

            time = response.xpath(
                "(//div[@class='tourNameBtn matchDateInfo']/span[2]/text())[1]").get()
            yield {


                "cham": champ,
                "teamA": teamA,
                "teamB": teamB,
                "time": time,
                "Result": teamAR + "-"+teamBR,



            }
        except:
            pass
