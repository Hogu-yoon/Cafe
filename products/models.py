from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from users.models import Profile


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_user')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products_user_profile', blank=True)
    name = models.CharField('품목', max_length=128)
    category = models.CharField('카테고리', max_length=128)
    information = models.TextField('상품정보')
    image = models.ImageField('상품사진', upload_to='product/', default='default.png')
    wish = models.ManyToManyField(User, related_name='products_wish', blank=True)
    published_date = models.DateTimeField(default=timezone.now)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    comment = models.TextField()
