import requests
import json
url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON"

resp = requests.get(url)

js = resp.json()
print(js["Table"]["Row"])
