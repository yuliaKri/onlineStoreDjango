from django.urls import path
from .views import *

urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('category/add/', CategoryCreate.as_view()),
    path('category/<int:pk>/', CatagoryRUD.as_view()),
    path('category/get/<int:pk>/', CategoryRetrieve.as_view()),
    path('get/<int:pk>/', ProductRetrieve.as_view()),
    path('category/<int:category_id>/products/', ProductListByCategory.as_view()),
    path('all/', ProductList.as_view()),
    path('brands/get/<int:pk>/', BrandRetrieve.as_view()),
]