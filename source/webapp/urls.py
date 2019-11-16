from django.urls import path
from webapp.views import product_views

app_name = 'webapp'

urlpatterns = [
    path('', product_views.index, name='index')
    ]
