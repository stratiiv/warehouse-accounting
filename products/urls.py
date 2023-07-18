from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import api_views
from . import views

# register API endpoints
router = DefaultRouter()
router.register(r'products', api_views.ProductViewSet)
router.register(r'categories', api_views.CategoryViewSet)

# API URL patterns
urlpatterns = [
    path('api/v1/', include(router.urls)),
]

# Regular view URL patterns
urlpatterns += [
    path('products/list/', views.ProductListView.as_view(), name="product-list"),
    path('products/search/', views.ProductSearchView.as_view(), name="product-search"),
    path('products/add/', views.ProductCreateView.as_view(), name="product-add"),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name="product-delete"),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name="product-update"),
    path('categories/list/', views.CategoryListView.as_view(), name="category-list"),
    path('categories/search/', views.CategorySearchView.as_view(), name="category-search"),
    path('categories/add/', views.CategoryCreateView.as_view(), name="category-add"),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name="category-delete"),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category-update"),
]

# Static media URL patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
