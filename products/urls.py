from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import api_views
from . import views

router = DefaultRouter()
router.register(r'products', api_views.ProductViewSet)
router.register(r'categories', api_views.CategoryViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('products/list/', views.ProductListView.as_view(), name="product-list"),
    path('products/add/', views.ProductCreateView.as_view(), name="product-add"),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name="product-delete"),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name="product-update"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
