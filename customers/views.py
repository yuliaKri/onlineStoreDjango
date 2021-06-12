from django.shortcuts import HttpResponse
from rest_framework import generics, permissions
from .serializers import CustomerSerializer
from .models import Customer
import uuid
import json

# домашка: скачать фронт и запустить на port 3000

def customer_create(request):
    if request.method == "POST":
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token=customer_token)
            response = {
                "status": True,
                "customer_token": customer_token
            }
        except BaseException:
            response = {"status": False}
    else:
        response = {"status": False, "message": "else"}

    return HttpResponse(json.dumps(response))



class CustomerList(generics.ListAPIView): # for admin only
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAdminUser]