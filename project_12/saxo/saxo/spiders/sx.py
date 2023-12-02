import scrapy
import json

class SxSpider(scrapy.Spider):
    name = "sx"
    allowed_domains = ["www.saxo.com"]
    # start_urls = ["https://www.saxo.com"]

    def start_requests(self):
        for i in range (1,80):
            url='https://www.saxo.com/dk/bestsellers/filter'
            payload = {"Filters": {
            "BaseFilterType": None,
            "BaseFilterId": None,
            "SortFilterParameters": [],
            "SelectedSortFilterValue": None,
            "ExternalFilterParameters": [],
            "SelectedExternalFilterValue": None,
            "SelectedCategoryFilterValue": None,
            "SelectedSerieFilterValue": None,
            "FormatFilterParameters": [],
            "SelectedFormatFilterValues": [],
            "LanguageFilterParameters": [
                {
                    "Id": "1166",
                    "Value": "dansk",
                    "Name": "Dansk",
                    "Type": 2,
                    "Hits": 18136,
                    "Selected": False,
                    "HitsLabel": "5.000+"
                },
                {
                    "Id": "1176",
                    "Value": "engelsk",
                    "Name": "Engelsk",
                    "Type": 2,
                    "Hits": 4440,
                    "Selected": False,
                    "HitsLabel": "4.000+"
                },
                {
                    "Id": "1172",
                    "Value": "hollandsk",
                    "Name": "Hollandsk",
                    "Type": 2,
                    "Hits": 12,
                    "Selected": False,
                    "HitsLabel": "12"
                },
                {
                    "Id": "1192",
                    "Value": "fransk",
                    "Name": "Fransk",
                    "Type": 2,
                    "Hits": 8,
                    "Selected": False,
                    "HitsLabel": "8"
                },
                {
                    "Id": "1200",
                    "Value": "tysk",
                    "Name": "Tysk",
                    "Type": 2,
                    "Hits": 6,
                    "Selected": False,
                    "HitsLabel": "6"
                },
                {
                    "Id": "1343",
                    "Value": "spansk",
                    "Name": "Castiliansk",
                    "Type": 2,
                    "Hits": 3,
                    "Selected": False,
                    "HitsLabel": "3"
                }
            ],
            "SelectedLanguageFilterValues": [],
            "CategoryFilterParameters": [
                {
                    "Id": "0",
                    "Value": "skoenlitteratur-og-relaterede-emner",
                    "Name": "Skønlitteratur og relaterede emner",
                    "Type": 3,
                    "Hits": 2090,
                    "Selected": False,
                    "HitsLabel": "2.000+"
                },
                {
                    "Id": "0",
                    "Value": "skoenlitteratur-generelt",
                    "Name": "Skønlitteratur: generelt",
                    "Type": 3,
                    "Hits": 1237,
                    "Selected": False,
                    "HitsLabel": "1.000+"
                },
                {
                    "Id": "0",
                    "Value": "krimier-og-mysterier",
                    "Name": "Krimier og mysterier",
                    "Type": 3,
                    "Hits": 655,
                    "Selected": False,
                    "HitsLabel": "655"
                },
                {
                    "Id": "0",
                    "Value": "samfund-og-samfundsvidenskab",
                    "Name": "Samfund og samfundsvidenskab",
                    "Type": 3,
                    "Hits": 626,
                    "Selected": False,
                    "HitsLabel": "626"
                },
                {
                    "Id": "0",
                    "Value": "moderne-skoenlitteratur-samtidslitteratur",
                    "Name": "Moderne skønlitteratur. Samtidslitteratur",
                    "Type": 3,
                    "Hits": 555,
                    "Selected": False,
                    "HitsLabel": "555"
                },
                {
                    "Id": "0",
                    "Value": "romantisk-skoenlitteratur",
                    "Name": "Romantisk skønlitteratur",
                    "Type": 3,
                    "Hits": 478,
                    "Selected": False,
                    "HitsLabel": "478"
                },
                {
                    "Id": "0",
                    "Value": "skoenlitteratur-specielle-litteraere-former",
                    "Name": "Skønlitteratur: specielle litterære former",
                    "Type": 3,
                    "Hits": 472,
                    "Selected": False,
                    "HitsLabel": "472"
                },
                {
                    "Id": "0",
                    "Value": "sundhed-relationer-og-personlig-udvikling",
                    "Name": "Sundhed, relationer og personlig udvikling",
                    "Type": 3,
                    "Hits": 436,
                    "Selected": False,
                    "HitsLabel": "436"
                },
                {
                    "Id": "0",
                    "Value": "thrillere-spaendingsromaner",
                    "Name": "Thrillere / spændingsromaner",
                    "Type": 3,
                    "Hits": 428,
                    "Selected": False,
                    "HitsLabel": "428"
                },
                {
                    "Id": "0",
                    "Value": "oversat-skoenlitteratur",
                    "Name": "Oversat skønlitteratur ",
                    "Type": 3,
                    "Hits": 390,
                    "Selected": False,
                    "HitsLabel": "390"
                },
                {
                    "Id": "0",
                    "Value": "biografier-litteratur-og-litteraturstudier",
                    "Name": "Biografier, litteratur og litteraturstudier",
                    "Type": 3,
                    "Hits": 387,
                    "Selected": False,
                    "HitsLabel": "387"
                },
                {
                    "Id": "0",
                    "Value": "livsstil-hobby-og-fritid",
                    "Name": "Livsstil, hobby og fritid",
                    "Type": 3,
                    "Hits": 376,
                    "Selected": False,
                    "HitsLabel": "376"
                },
                {
                    "Id": "0",
                    "Value": "oekonomi-finans-erhvervsliv-og-ledelse",
                    "Name": "Økonomi, finans, erhvervsliv og ledelse",
                    "Type": 3,
                    "Hits": 318,
                    "Selected": False,
                    "HitsLabel": "318"
                },
                {
                    "Id": "0",
                    "Value": "biografier-og-sande-fortaellinger",
                    "Name": "Biografier og sande fortællinger",
                    "Type": 3,
                    "Hits": 315,
                    "Selected": False,
                    "HitsLabel": "315"
                },
                {
                    "Id": "0",
                    "Value": "boerneboeger-ungdomsboeger-og-undervisningsmidler",
                    "Name": "Børnebøger, ungdomsbøger og undervisningsmidler",
                    "Type": 3,
                    "Hits": 298,
                    "Selected": False,
                    "HitsLabel": "298"
                },
                {
                    "Id": "0",
                    "Value": "historiske-romaner",
                    "Name": "Historiske romaner",
                    "Type": 3,
                    "Hits": 276,
                    "Selected": False,
                    "HitsLabel": "276"
                },
                {
                    "Id": "0",
                    "Value": "erhvervsliv-virksomheder-og-ledelse",
                    "Name": "Erhvervsliv, virksomheder og ledelse",
                    "Type": 3,
                    "Hits": 258,
                    "Selected": False,
                    "HitsLabel": "258"
                },
                {
                    "Id": "0",
                    "Value": "familie-og-sundhed",
                    "Name": "Familie og sundhed",
                    "Type": 3,
                    "Hits": 249,
                    "Selected": False,
                    "HitsLabel": "249"
                },
                {
                    "Id": "0",
                    "Value": "samfund-og-kultur-generelt",
                    "Name": "Samfund og kultur: generelt",
                    "Type": 3,
                    "Hits": 234,
                    "Selected": False,
                    "HitsLabel": "234"
                },
                {
                    "Id": "0",
                    "Value": "skoenlitteratur-narrative-temaer",
                    "Name": "Skønlitteratur: narrative temaer",
                    "Type": 3,
                    "Hits": 226,
                    "Selected": False,
                    "HitsLabel": "226"
                }
            ],
            "SelectedCategoryFilterValues": [],
            "ContributorFilterParameters": [],
            "SelectedContributorFilterValues": [],
            "PublisherFilterParameters": [],
            "SelectedPublisherFilterValues": [],
            "ProductTypeFilterParameters": [
                {
                    "Id": "1",
                    "Value": "bog",
                    "Name": "Bøger",
                    "Type": 1,
                    "Hits": 264532,
                    "Selected": False,
                    "HitsLabel": "5.000+"
                },
                {
                    "Id": "5",
                    "Value": "e-bog",
                    "Name": "E-bøger",
                    "Type": 1,
                    "Hits": 22718,
                    "Selected": True,
                    "HitsLabel": "5.000+"
                },
                {
                    "Id": "10",
                    "Value": "lydbog",
                    "Name": "Lydbøger",
                    "Type": 1,
                    "Hits": 7425,
                    "Selected": False,
                    "HitsLabel": "5.000+"
                }
            ],
            "SelectedProductTypeFilterValues": [
                {
                    "Id": "5",
                    "Value": "e-bog",
                    "Name": "E-bøger",
                    "Type": 1,
                    "Hits": 22718,
                    "Selected": True,
                    "HitsLabel": "5.000+"
                }
            ],
            "Query": None,
            "IsOrderable": False,
            "PageSize": 32,
            "PageIndex": i,
            "FilteredProductsTotalCount": 0,
            "FilteredProductsTotalCountString": "0",
            "IsAnyFilterApplied": True
        }}

            headers = {
                "User-Agent": "PostmanRuntime/7.35.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "en-US,en;q=0.5",
                # "Accept-Encoding": "gzip, deflate, br",
                "X-NewRelic-ID": "VgAAV1BbGwcGUlBXDwME",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.saxo.com",
                "Connection": "keep-alive",
                "Referer": "https://www.saxo.com/dk/bestsellere?pt=e-bog",
                "Cookie": "showPremiumBanner=true; ASP.NET_SessionId=oc0dgpspqlpszjjcgrtspy0i; saxo_cart_is_empty=yes; _gcl_au=1.1.1565188550.1700306338; CookieConsent={stamp:%27XG6MinD1LSh34P9kNcPr5TBGbXFVWCCXb32f1pYaBRoRoxR/UfKbgw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1700306338950%2Cregion:%27eg%27}; _ga_MXLY381H2N=GS1.1.1700306340.1.1.1700306903.0.0.0; _ga=GA1.1.2137141065.1700306341; _pk_id.4.7785=f5a5b0eca1c88e1b.1700306341.; _pk_ses.4.7785=1; __exponea_etc__=1052b893-cb68-4654-8412-00bca5ede5c7; __exponea_time2__=-0.9561388492584229; _fbp=fb.1.1700306342050.1513110190; BIGipServer~saxo~pool-saxo-https=1359472138.47873.0000; saxo_rsc=eF5jYSlN9kg0SrYwSzNO1U0xMzTRNTFNSdG1SEuz0E01NjNKs7BIMjNNtODKLSvJTOEzNTTWNdQ1BACY8Q54; _uetsid=46a1f870860411ee93deb92ca57df0ab; _uetvid=46a22a80860411eeb994897db332c227",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "Content-Type": "application/json"
            }
            
            yield scrapy.Request(url,method="POST",body=json.dumps(payload),headers=headers,callback=self.parse)
            
    
    def parse(self, response):
        books=response.json()["Products"]
        for book in books:
            title=book["Title"]
            Rank=book["Rank"]
            AuthorName=book["AuthorName"]
            Id=book["Id"]
            Price_normal=book["Price"]["PriceNormal"]
            Language=book["Language"]["Name"]
            
            yield {
                "Rank":Rank,
                "title":title,
                "AuthorName":AuthorName,
                "Language":Language,
                "Price_normal":Price_normal,
                "Id":Id,
            }