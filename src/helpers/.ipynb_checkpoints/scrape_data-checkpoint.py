from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
# option.add_argument('--headless')

url = 'https://www.amazon.in/Centrino-Mens-CHICKU-Sneaker-9-3322-22/dp/B08Z48P1XZ/?_encoding=UTF8&pd_rd_w=DXJkl&content-id=amzn1.sym.4f3c73a8-dac5-4181-8aa7-51fa268716c9%3Aamzn1.symc.cdb151ed-d8fe-485d-b383-800c8b0e3fd3&pf_rd_p=4f3c73a8-dac5-4181-8aa7-51fa268716c9&pf_rd_r=MXBR14RDD5XNXFMAP2BF&pd_rd_wg=8mmrz&pd_rd_r=b7c68d21-4952-44a8-bbfd-a32e4169e756&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

def scrape(url):
    with webdriver.Chrome(options=option) as driver:
        driver.get(url) #HTTP Request
        html = driver.page_source
    return html