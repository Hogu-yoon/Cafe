from rest_framework import serializers

from products.models import Product, Review
from users.serializers import ProfileSerializer


class ReviewSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["pk", 'profile', 'product', 'comment']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["product", "comment"]


class ProductSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    # 변수이름 related_name으로 쓸것~!!!!!!
    product_review = ReviewSerializer(many=True, read_only=True)
    # 리뷰를 추가 하고 다수의 리뷰를 볼수있게.
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
        fields = (
            "pk",
            "profile",
            "name",
            "information",
            "image",
            "published_date",
            "wish",
            "product_review",
            "category",
        )


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "category", "information", "image"]
