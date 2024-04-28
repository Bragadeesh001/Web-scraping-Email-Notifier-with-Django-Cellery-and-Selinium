from rest_framework import serializers
from .models import UserDetail, ProductDetails, ProductRating

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['id', 'user', 'email', 'url', 'created']

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['id', 'user', 'product_dimension', 'date_first_available', 'manufacturer', 'asin', 'model_number', 'origin_country', 'department', 'packer', 'importer', 'item_weight', 'item_dimension', 'net_quantity', 'generic_name']

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ['id', 'product_details', 'rating', 'total_raters']