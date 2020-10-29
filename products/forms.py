from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        # assign Product model, all fields
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # override default __init__
        super().__init__(*args, **kwargs)
        # assign Category model
        categories = Category.objects.all()
        # list comprehension to create tuple of friendly names from categories
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # display friendly name instead of category
        self.fields['category'].choices = friendly_names
        # assign css classes to each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
