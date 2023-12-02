from bs4 import BeautifulSoup
import json
from playwright.sync_api import sync_playwright
import pandas as pd




def extract_full_body_html(u):
    # url = 'https://www.qatarliving.com/backend/api/properties/search?from=1&category=7642'
    Timeout = 90000

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(u)

        # page.wait_for_load_state("networkidle", timeout=Timeout)
        # page.wait_for_timeout(1000)
        page.wait_for_timeout(2500)
        return page.inner_text('body')


# def extract_budget(html):
#     soup = BeautifulSoup(html, 'lxml')
#     budget_div = soup.select('div.visualization-section__data')[0]
#     return budget_div.get_text()

t=[]
p=[]
e=[]
pr=[]
for i in range(1,10):
    url = f'https://www.qatarliving.com/backend/api/properties/search?from={i}&category=7642'
    a=json.loads(extract_full_body_html(url))["properties"]
    print(i)
    for item in a:
        title=item["_source"]["title"]
        t.append(title)
        phone=item["_source"]["phone"]
        p.append(phone)
        email=item["_source"]["email"]
        e.append(email)
        price=item["_source"]["price"]
        pr.append(price)
        
# print(extract_full_body_html(url))
print(len(t))
print(len(p))
print(len(e))
print(len(pr))

dd={
    "title":t,
    "phone":p,
    "email":e,
    "price":pr,
}

df=pd.DataFrame.from_dict(dd)
df.to_csv("ssss.csv",index=False)