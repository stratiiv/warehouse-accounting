from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "product_list"
    template_name = "products/product_list.html"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "category", "image"]
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'image']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy("product-list")


class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = "category_list"
    template_name = "categories/category_list.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ["name", "description"]
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")
    

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy("category-list")
