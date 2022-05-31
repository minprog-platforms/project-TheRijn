from django import forms
from .models import Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = Category
        fields = "__all__"
