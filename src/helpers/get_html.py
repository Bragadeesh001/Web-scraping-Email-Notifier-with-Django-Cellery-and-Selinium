from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless=new')



def scrape(url):
    with webdriver.Chrome(options=option) as driver:
        driver.get(url) #HTTP Request
        html = driver.page_source
    return html