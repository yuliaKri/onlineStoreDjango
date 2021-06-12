from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .serializers import *
from .filters import *
from .models import Category, Product, ProductCategory, Brand
from .paginations import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend


# добить на вторник - приведите все методы и классы и сериалайзеры для каждой модели, заказов, клиентов
# cм. фильтры и сортировки


class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    def get_queryset(self): # permition we may define here - it's an example that here we can peredefine method
        return Category.objects.filter(is_active=True)


class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()


class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class = ProductSerializer # ProductRetrieveSerializer
    queryset = Product.objects.all()


class ProductList(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    # filterset_fields = ['brand', 'price'] # http://127.0.0.1:8000/api/product/all/?brand=1
    search_fields = ['title'] # http://127.0.0.1:8000/api/product/all/?search=Product%201
    ordering_fields = ['title', 'price', 'old_price'] # http://127.0.0.1:8000/api/product/all/?ordering=price or -price


class BrandRetrieve(generics.RetrieveAPIView):
    serializer_class = BrandRetrieveWithProductSerializer
    queryset = Brand.objects.all()


######################################################################################################
# Code below is under danger only for admin and study usage. Delete before deployed
# почитать про urm - относится к django
# как делать связанные выборки с помошью сериализации продукты - связанные с категориями через ForeignKey
######################################################################################################

class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CatagoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def delete(self, request, *args, **kwargs):
        #try:
        return Response({"message": "record deleted"}, status=status.HTTP_200_OK)
        #except BaseException as error:
        #    return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)


class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer

    def get_queryset(self):
        product_ids = ProductCategory.objects.filter(category_id=self.kwargs['category_id']).values('product_id')
        return Product.objects.filter(pk__in=product_ids)
    #SELECT * FROM products WHERE id in (1,2,3)

#def test_view(request):
# x = Product.objects.filter(brand__id=1) or  x = Product.objects.get(id=1) or
# x = Product.objects.filter(price__gte=100, price__lte=20, brand__id=2)print(el.price, el.title, el.brand, 'product_id = '+el.id)
# x = Product.objects.filter(price__gte=150, price__lte=20)
#>>> for el in x:
#...     el.price += 2
#...     print(el)
#...     el.save()
# create
#Product.objects.create(title='Product 8', price=300.00, quantity=1)
#<Product: Product 8>
#>>> x = Product.objects.get(id=9)
#>>> x.brand = br
#>>> x.save()
#gt  - Greater than.
#gte - Greater than or equal to.
#lt - Less than.
#lte - Less than or equal to.




