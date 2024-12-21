from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response([{"id": product.id, "name": product.name, "price": product.price} for product in products])