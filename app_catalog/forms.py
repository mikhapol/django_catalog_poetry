from django import forms

from app_catalog.models import Product, Provider, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_actual' and field_name != 'published' and field_name != 'closed':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар',)

    class Meta:
        model = Product
        fields = ('name', 'desc', 'image', 'category', 'price', 'owner')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if any(word in cleaned_data.lower() for word in self.forbidden_words):
            raise forms.ValidationError('Запрещенное слово в названии')
        return cleaned_data

    def clean_desc(self):
        cleaned_data = self.cleaned_data['desc']
        if any(word in cleaned_data.lower() for word in self.forbidden_words):
            raise forms.ValidationError('Запрещенное слово в описании')
        return cleaned_data


class ProviderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
