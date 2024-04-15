import datetime

from django import forms


class ProductForm(forms.Form):
    id_product = forms.IntegerField(min_value=1)
    # id_product = forms.ModelChoiceField(label="Product",
    #                                     queryset=Product.objects.all(),
    #                                     to_field_name="pk")
    name_product = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите наименование продукта'}))
    description = forms.CharField(max_length=1500,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'описание продукта'}))
    price = forms.FloatField(min_value=0,
                             widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'стоимость за '
                                                                                                     'еденицу'}))
    quantity = forms.IntegerField(min_value=0,
                                  widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'количество'}))
    date_add = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date',
                                                             'placeholder': 'дата добавления продукта'}))
    image_product = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'изображение продукта'}))
    file_product = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-check-input',
                                                                 'placeholder': 'к-н файл для теста загр. в др. папку'}))
    is_active = forms.BooleanField(required=True,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
