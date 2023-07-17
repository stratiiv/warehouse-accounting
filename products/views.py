from django.views.generic import ListView
from .models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "product_list"
    template_name = "products/product_list.html"


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = "category_list"
    template_name = "products/category_list.html"