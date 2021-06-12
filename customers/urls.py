from django.urls import path
from .views import *

urlpatterns = [
    path('list/', CustomerList.as_view()),
    path('create/', customer_create)
]