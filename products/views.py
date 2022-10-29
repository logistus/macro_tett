from dataclasses import fields
from django.shortcuts import render
from products.models import Product
from django.views import generic
from django.urls import reverse_lazy
from products.forms import CreateProductForm


def home(request):
    products = Product.objects.all().order_by('expiry_date')
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


class ProductListView(generic.ListView):
    model = Product
    fields = ['product_image', 'expiry_date']
    queryset = Product.objects.all().order_by('expiry_date')
    context_object_name = 'products'


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class ProductCreateView(generic.CreateView):
    model = Product
    success_url = reverse_lazy('products')
    form_class = CreateProductForm
