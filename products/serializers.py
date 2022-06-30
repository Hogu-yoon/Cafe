from rest_framework import serializers

from products.models import Product
from users.serializers import ProfileSerializer


class ProductSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    '''
    seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products_user')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='products_user_profile',blank=True)
    name = models.CharField('품목',max_length=128)
    category = models.CharField('카테고리',max_length=128)
    information = models.TextField('상품정보')
    image = models.ImageField('상품사진',upload_to='product/', default='default.png')
    wish = models.ManyToManyField(User ,related_name='products_wish', blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    '''

    class Meta:
        model = Product
        fields = ["pk", "profile", "name", "information", "image", "published_date", "wish"]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "category", "information", "image"]

