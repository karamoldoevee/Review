from django.urls import path
from webapp.views import product_views, review_views

app_name = 'webapp'

urlpatterns = [
    path('', product_views.IndexView.as_view(), name='index'),
    path('product/<int:pk>/', product_views.ProductView.as_view(), name='product_view'),
    path('product/add/', product_views.ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/change/', product_views.ProductUpdateView.as_view(), name='product_change'),
    path('product/<int:pk>/delete/', product_views.ProductDeleteView.as_view(), name='product_delete'),
    path('comments/', review_views.ReviewListView.as_view(), name='review_list'),
    path('comment/add/',review_views.ReviewListView.as_view(), name='review_add'),
    path('comment/<int:pk>/сhange/', review_views.ReviewtUpdateView.as_view(), name='review_change'),
    path('comment/<int:pk>/delete/', review_views.ReviewtDeleteView.as_view(), name='review_delete'),
    path('article/<int:pk>/add-comment/', review_views.ReviewForProductCreateView.as_view(), name='product_review_add'),
    ]
