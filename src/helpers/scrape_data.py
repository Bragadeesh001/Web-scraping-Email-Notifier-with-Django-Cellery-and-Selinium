from bs4 import BeautifulSoup
from .get_html import scrape

url = 'https://www.amazon.in/Centrino-Mens-CHICKU-Sneaker-9-3322-22/dp/B08Z48P1XZ/?_encoding=UTF8&pd_rd_w=DXJkl&content-id=amzn1.sym.4f3c73a8-dac5-4181-8aa7-51fa268716c9%3Aamzn1.symc.cdb151ed-d8fe-485d-b383-800c8b0e3fd3&pf_rd_p=4f3c73a8-dac5-4181-8aa7-51fa268716c9&pf_rd_r=MXBR14RDD5XNXFMAP2BF&pd_rd_wg=8mmrz&pd_rd_r=b7c68d21-4952-44a8-bbfd-a32e4169e756&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

html = scrape(url)

soup = BeautifulSoup(html)

def product_title():
    productTitle = soup.find('span', id='productTitle')
    return productTitle.text.strip()

def product_price():
    try:
        if soup.find_all('span', {'class':'a-price-whole'}):
            productPrice = soup.find_all('span', {'class':'a-price-whole'})[0].text
        elif soup.find_all('span', {'id': 'a-price-whole'}):
            productPrice = soup.find_all('span', {'id': 'a-price-whole'})[0].text
        else:
            productPrice = ''
    except Exception as e:
        print(e)
        productPrice = ''
    return productPrice

def product_details():
    try:
        productDetails={}
        all_tag = soup.find('div', id='detailBullets_feature_div')
        all_li = all_tag.find_all('li')
        for li in all_li:
            list_values = li.find_all('span')
            key = list_values[1].text.split('\n')[0]
            value = list_values[2].text.split('\n')[0]
            productDetails[key] = value
        return productDetails
                
    except Exception as e:
        print(e)
        return {}

def product_review():
    all_tag = soup.find('div', id='cm_cr_dp_d_rating_histogram')
    rating = all_tag.find('span', {'data-hook': 'rating-out-of-text'}).text.split(' ')[0]
    total_rating = all_tag.find('span', {'data-hook': 'total-review-count'}).text.split(' ')[0]
    productReview = {
        'rating': rating,
        'total_rating': total_rating,
    }
    return productReview
