from django import forms

from webapp.models import Product, Review



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']

    def clean_summary(self):
        title = self.cleaned_data['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'raiting']

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")