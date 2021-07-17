from django import forms

from app_2.models import Companies


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=128, label="Nazwa")
    price = forms.IntegerField(label="Cena")
    date = forms.DateField()


class SearchForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Companies.objects.all(), label='Nazwa')
    date_from = forms.DateField()
    date_to = forms.DateField()
