from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product