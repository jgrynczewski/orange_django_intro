from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mainapp.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy('list_view')
