import requests

url = "https://www.tax.service.gov.uk/check-register-fair-rents/search"

payload = 'csrfToken=88f52d895d412e742e5951abfa626a13bb6b3711-1698776780452-760755e97cca78d06f6cadb4&q=da1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.tax.service.gov.uk/check-register-fair-rents/search?_ga=2.174123170.1467572594.1698776620-714798677.1698776620',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.tax.service.gov.uk',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
