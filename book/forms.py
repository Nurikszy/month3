from django import forms
from . import models

class BookForm(forms.Form):
    class Meta:
        model = models.Book
        fields = "__all__"