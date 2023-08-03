from django import forms

from catalog_app.models import Version
from catalog_app.models.products import Product
from catalog_app.models.provider import Provider


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар',):
            raise forms.ValidationError('Данный продукт не моет быть добавлен')
        return cleaned_data

    def clean_desc(self):
        cleaned_data = self.cleaned_data['desc']
        if cleaned_data in ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар',):
            raise forms.ValidationError('Описание плохое')
        return cleaned_data


class ProviderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
