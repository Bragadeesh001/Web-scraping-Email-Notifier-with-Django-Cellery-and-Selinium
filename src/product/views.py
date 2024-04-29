from rest_framework import viewsets
from .models import UserDetail
from .serializers import UserDetailSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
