from django.urls import path
from webapp.views import product_views

app_name = 'webapp'

urlpatterns = [
    path('', product_views.IndexView.as_view(), name='index'),
    path('product/<int:pk>/', product_views.ProductView.as_view(), name='product_view'),
    path('product/add/', product_views.ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/change/', product_views.ProductUpdateView.as_view(), name='product_change'),
    path('product/<int:pk>/delete/', product_views.ProductDeleteView.as_view(), name='product_delete'),
    ]
