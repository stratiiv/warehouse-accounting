from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Product, Category


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "product_list"
    template_name = "products/product_list.html"


class ProductSearchView(ListView):
    model = Product 
    template_name = "products/product_list.html"
    context_object_name = "product_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) |
                                       Q(category__name__icontains=search_query))
        return queryset


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


class CategorySearchView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "category_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) |
                                       Q(description__icontains=search_query))
        return queryset


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
