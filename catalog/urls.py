from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('product/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
]