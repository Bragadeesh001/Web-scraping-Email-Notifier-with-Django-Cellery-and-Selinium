from celery import shared_task
from django.apps import apps
from helpers import get_html
from helpers import scrape_data
from bs4 import BeautifulSoup


@shared_task
def scrape_product_url_task(url,  pk):
    try:
        user_model = apps.get_model('UserDetail')
        User = user_model.objects.get(pk=pk)
        html = get_html.scrape(url)
        soup = BeautifulSoup(html)
        data = scrape_data.product_details(soup)
        corrected_data = {
            'price': data['price'],
            'product_dimension': data['Product Dimensions'],
            'date_first_available': data['Date First Available'],
            'manufacturer': data['Manufacturer'],
            'asin':data['ASIN'],
            'model_number': data['Item model number'],
            'origin_country': data['Country of Origin'],
            'department': data['Department'],
            'packer': data['Packer'],
            'importer': data['importer'],
            'item_weight': data['Item Weight'],
            'item_dimension': data['Item Dimensions LxWxH'],
            'net_quantity': data['Net Quantity'],
            'generic_name': data['Generic Name']
        }
        model = apps.get_model('ProductDetails')
        model.objects.create(user = User, **corrected_data)
        data = scrape_data.product_rating(soup)
        product = model.objects.get(user=User)
        model = apps.get_model('ProductRating')
        model.objects.create(product_details = product, **data)
    except Exception as e:
        print('Error caused at celery scrape due to ', e)
