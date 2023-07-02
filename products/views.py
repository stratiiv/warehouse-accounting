from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    """Provides CRUD endpoints on Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        """Auto add current user when creating product"""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Auto add current user when updating product"""
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    """Provides CRUD endpoints on Category"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
