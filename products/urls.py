from django.urls import path

from rest_framework import routers

from products.views import ProductViewSet, wish_product, ReviewViewSet

router = routers.SimpleRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls + [
    path('wish/<int:pk>/',wish_product, name='wish_product')
]
