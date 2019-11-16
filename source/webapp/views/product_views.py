from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.forms import SimpleSearchForm
from webapp.models import Product

from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

    paginate_by = 3

    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()

        self.search_value = self.get_search_value()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):

        queryset = super().get_queryset()

        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(category__icontains=self.search_value)

            queryset = queryset.filter(query)

        return queryset

    def get_search_form(self):

        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):

        if self.form.is_valid():
            return self.form.cleaned_data['search']

        return None


class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'

class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/add.html'
    fields = ('name', 'category', 'description', 'image')
    permission_required = 'webapp.add_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/change.html'
    fields = ('name', 'category', 'description', 'image')
    context_object_name = 'product'
    permission_required = 'webapp.change_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin,DeleteView):

    template_name = 'product/delete.html'

    model = Product

    context_object_name = 'product'

    success_url = reverse_lazy('webapp:index')

    permission_required = 'webapp.delete_product'

    permission_denied_message = "Доступ запрещён"




