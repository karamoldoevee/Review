from django import forms

from webapp.models import Product, Review
from django.forms import Select


class IssueForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(widget=Select, required=False, empty_label=None, queryset=None)

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']

    def clean_summary(self):
        title = self.cleaned_data['name']

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")