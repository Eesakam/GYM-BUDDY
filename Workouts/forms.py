from django.forms import CheckboxInput, DateField, ModelForm, DateInput,forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Submit, Row, Column
from datetime import date
from django import forms
from .models import Workout,Category


class CategoryEditForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ["C_time","Workout"]