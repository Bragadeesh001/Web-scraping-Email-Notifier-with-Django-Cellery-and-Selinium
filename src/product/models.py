from django.db import models
from django.contrib.auth.models import User
from product import tasks

class UserDetail(models.Model):
    user = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False, max_length=255)
    url = models.URLField(max_length=500)
    created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print('After save - URL:', self.url, 'PK:', self.pk)
        if self.url:
            print('value', self.url, self.pk)
            tasks.scrape_product_url_task.delay(self.url, self.pk)


class ProductDetails(models.Model):
    user = models.ForeignKey(UserDetail, related_name='products', on_delete=models.CASCADE)
    price = models.CharField(max_length=255, blank=True)
    product_dimension = models.CharField(max_length=255, blank=True)
    date_first_available = models.CharField(max_length=255,null=True, blank=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    asin = models.CharField(max_length=255, blank=True)
    model_number = models.CharField(max_length=255, blank=True)
    origin_country = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    packer = models.CharField(max_length=255, blank=True)
    importer = models.CharField(max_length=255, blank=True)
    item_weight = models.CharField(max_length=255, blank=True)
    item_dimension = models.CharField(max_length=255, blank=True)
    net_quantity = models.CharField(max_length=255, blank=True)
    generic_name = models.CharField(max_length=255, blank=True)

class ProductRating(models.Model):
    product_details = models.OneToOneField(ProductDetails, on_delete=models.CASCADE, related_name='ratings')
    rating = models.CharField(max_length=255, blank=True)
    total_rating = models.CharField(max_length=255, blank=True)