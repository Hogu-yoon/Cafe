from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
# 필터 사용
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
# get 실패하면 404 코드 (DRF)
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Product, Review
from products.permissions import CustomReadOnly
from products.serializers import ProductSerializer, ProductCreateSerializer, ReviewSerializer, ReviewCreateSerializer
from users.models import Profile

from rest_framework import status

'''
제품 CRUD 
'''


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller', 'wish']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ProductSerializer
        return ProductCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(seller=self.request.user, profile=profile)


'''
제품 찜하기 기능
'''


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user in product.wish.all():
        product.wish.remove(request.user)
    else:
        product.wish.add(request.user)

    return Response(status=status.HTTP_200_OK)


'''
제품 후기 CRUD + permission
'''


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ReviewSerializer
        return ReviewCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)
