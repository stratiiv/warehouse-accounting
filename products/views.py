from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import (PermissionRequiredMixin,
                                        LoginRequiredMixin)
from .models import Product, Category
from .permissions import has_edit_permission


class ProductListView(ListView):
    """
    Display a list of all products.
    """
    queryset = Product.objects.all()
    context_object_name = "product_list"
    template_name = "products/product_list.html"


class ProductSearchView(ListView):
    """
    Display a list of products filtered by search query.
    """
    model = Product 
    template_name = "products/product_list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            name_filter = Q(name__icontains=search_query)
            category_name_filter = Q(category__name__icontains=search_query)
            queryset = queryset.filter(name_filter | category_name_filter)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new product.
    """
    model = Product
    fields = ["name", "category", "image"]
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, 
                        DeleteView):
    """
    Delete a product.
    """
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")

    def has_permission(self):
        product = self.get_object()
        return has_edit_permission(self.request, product)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                        UpdateView):
    """
    Update an existing product.
    """
    model = Product
    fields = ['name', 'category', 'image']
    template_name = 'products/product_form.html'
    success_url = reverse_lazy("product-list")

    def has_permission(self):
        product = self.get_object()
        return has_edit_permission(self.request, product)


class CategoryListView(ListView):
    """
    Display a list of all categories.
    """
    queryset = Category.objects.all()
    context_object_name = "category_list"
    template_name = "categories/category_list.html"


class CategorySearchView(ListView):
    """
    Display a list of categories filtered by search query.
    """
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) |
                                       Q(description__icontains=search_query))
        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new category.
    """
    model = Category
    fields = ["name", "description"]
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a category.
    """
    model = Category
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing category.
    """
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy("category-list")
