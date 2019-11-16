from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView

from webapp.forms import ReviewForm, ProductReviewForm
from webapp.models import Product, Review


class ReviewListView(ListView):
    template_name = 'review/list.html'
    model = Review
    context_object_name = 'reviews'
    paginate_by = 5
    paginate_orphans = 3


class ReviewForProductCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ProductReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.product = self.get_product()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = self.product.review.create(
            author=self.request.user,
            **form.cleaned_data
        )
        return redirect('webapp:product_view', pk=self.product.pk)

    def get_product(self):
        product_pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=product_pk)


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class ReviewtUpdateView(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ProductReviewForm
    context_object_name = 'review'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author \
               or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class ReviewtDeleteView(DeleteView):
    model = Review

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author \
               or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})