from rest_framework import serializers
from .models import Category, Product, ProductReview, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'is_active']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class BrandField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'title': value.title}


class ProductSerializer(serializers.ModelSerializer):  # ProductRetrieveSerializer
    reviews = ProductReviewSerializer(many=True, read_only=True)
    brand = BrandField(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'quantity', 'photo', 'brand', 'description', 'reviews']


class ProductPreviewSerializer(serializers.ModelSerializer):
    brand = BrandField(many=False, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'photo', 'brand']

class BrandRetrieveWithProductSerializer(serializers.ModelSerializer): # retrieve using when we want to get by id. not list
    products = ProductPreviewSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['id', 'title', 'products']
