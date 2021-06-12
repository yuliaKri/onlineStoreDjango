from django.urls import path
from .views import OrderList

urlpatterns = [
    path('list/', OrderList.as_view()),
   # path('product/list/', ProductList.as_view())
]