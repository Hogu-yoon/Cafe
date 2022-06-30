from django.urls import path

from rest_framework import routers

from products.views import ProductViewSet

router = routers.SimpleRouter()
router.register('posts', ProductViewSet)

urlpatterns = router.urls
