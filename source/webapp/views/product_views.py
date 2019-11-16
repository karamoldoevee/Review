from django.http import HttpResponseRedirect
from django.shortcuts import reverse

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product



class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/add.html'
    fields = ('name', 'category', 'description', 'image')

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/change.html'
    fields = ('name', 'category', 'description', 'image')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'product'

    def delete(self, request, *args, **kwargs):
        product = self.object = self.get_object()
        product.in_order = False
        product.save()
        return HttpResponseRedirect(self.get_success_url())




