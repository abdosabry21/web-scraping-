from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright





def extract_full_body_html(url):
    url = 'https://www.congress.gov/members?pageSize=250&page=1'
    Timeout = 90000

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout=Timeout)
        
        ht=page.inner_html('body')
        browser.close()
        return ht


def extract_budget(html):
    soup = BeautifulSoup(html, 'lxml')
    # names=soup.select("li.compact> span.result-heading > a")
    img=soup.select("li.compact>div.quick-search-member>div.member-image img")
    imgs=[]
    # namess=[]
    # for name in names:
    #     namess.append(name.get_text())
    #     imgs.append(name.__getattribute__("href"))
        # print('https://www.congress.gov/img'+name.get_attribute_list("href")[0])
        
    for photo in img:
        img_name=photo.get_attribute_list("src")[0].split(r"/")[-1]
        print(img_name)
        url_img='https://www.congress.gov'+photo.get_attribute_list("src")[0]
        img_down(url_img,img_name)
    




def img_down(link,name):
    # link = 'https://www.congress.gov/img/member/111brightb-al02_200.jpg'
    Timeout = 90000

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        res=page.goto(link)
        content=res.body()

        page.wait_for_load_state("networkidle", timeout=Timeout)
        # page.wait_for_selector(
        #     'div.visualization-section__data', timeout=Timeout)
        with open(f'{name}', 'wb') as f:
            f.write(content)
        




# "https://www.congress.gov/img/member/111brightb-al02_200.jpg"
# img_down("https://www.congress.gov/img/member/111brightb-al02_200.jpg")

for i in range(1,11):
    url = f'https://www.congress.gov/members?pageSize=250&page={i}'
    html = extract_full_body_html(url)
    extract_budget(html)
# # print(len(extract_budget(html)))