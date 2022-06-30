from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from products.models import Product
from products.permissions import CustomReadOnly
from products.serializers import ProductSerializer, ProductCreateSerializer
from users.models import Profile


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ProductSerializer
        return ProductCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(seller=self.request.user,profile=profile)