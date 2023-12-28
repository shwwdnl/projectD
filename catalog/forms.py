from django import forms

from catalog.models import Product, Version




class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'category')


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ('version_num', 'version_name', 'version_indication')
