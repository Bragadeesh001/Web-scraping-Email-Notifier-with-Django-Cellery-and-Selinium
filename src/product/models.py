from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    url = models.URLField()
    created = models.DateField(auto_now_add=True)

class ProductDetails(models.Model):
    user = models.ForeignKey(UserDetail, related_name='products', on_delete=models.CASCADE)
    product_dimension = models.CharField(max_length=255, blank=True)
    date_first_available = models.DateField(null=True, blank=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    asin = models.CharField(max_length=255, blank=True, unique=True)
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
    total_raters = models.CharField(max_length=255, blank=True)