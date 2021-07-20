from django import forms

from app_2.models import Companies


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=128, label="Nazwa")
    price = forms.IntegerField(label="Cena")
    date = forms.DateField()


class SearchForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Companies.objects.all().using("tes").distinct("name"), label='Nazwa')
    date_from = forms.DateField(required=False, label='Data od', help_text="yyyy-mm-dd")
    date_to = forms.DateField(required=False, label='Data do')
