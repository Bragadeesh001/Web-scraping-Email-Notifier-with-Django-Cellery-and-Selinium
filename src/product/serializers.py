from rest_framework import serializers
from .models import UserDetail, ProductDetails, ProductRating

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['user', 'email', 'url', 'created']
