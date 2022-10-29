from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/delete',
         views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/add', views.ProductCreateView.as_view(), name='product_add'),
]
