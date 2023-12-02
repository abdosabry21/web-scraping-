import json
import scrapy


class PubchemSpider(scrapy.Spider):
    name = "pubchem"
    allowed_domains = ["pubchem.ncbi.nlm.nih.gov"]
    start_urls = [
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON"]

    def parse(self, response):
        js = response.json()
        x = js.get('Table').get('Row')
        for i in range(0, len(x)):
            AtomicNumber = x[i]["Cell"][0]
            Symbol = x[i]["Cell"][1]
            Name = x[i]["Cell"][2]
            CPKHexColor = x[i]["Cell"][3]
            ElectronConfiguration = x[i]["Cell"][4]
            Electronegativity = x[i]["Cell"][5]
            AtomicRadius = x[i]["Cell"][6]
            IonizationEnergy = x[i]["Cell"][7]
            ElectronAffinity = x[i]["Cell"][8]
            OxidationStates = x[i]["Cell"][9]
            StandardState = x[i]["Cell"][10]
            MeltingPoint = x[i]["Cell"][11]
            BoilingPoint = x[i]["Cell"][12]
            Density = x[i]["Cell"][13]
            GroupBlock = x[i]["Cell"][14]
            YearDiscovered = x[i]["Cell"][15]

            yield {
                'Symbol': Symbol,
                'Name': Name,
                'AtomicNumber': AtomicNumber,
                'CPKHexColor': CPKHexColor,
                'ElectronConfiguration': ElectronConfiguration,
                'Electronegativity': Electronegativity,
                'AtomicRadius': AtomicRadius,
                'IonizationEnergy': IonizationEnergy,
                'ElectronAffinity': ElectronAffinity,
                'OxidationStates': OxidationStates,
                'StandardState': StandardState,
                'MeltingPoint': MeltingPoint,
                'BoilingPoint': BoilingPoint,
                'Density': Density,
                'GroupBlock': GroupBlock,
                'YearDiscovered': YearDiscovered,

            }
