from django.forms import ModelForm, CharField, TextInput
from .models import Author


class AuthorForm(ModelForm):
    fullname = CharField(max_length=100,
                         required=True,
                         widget=TextInput())
    born_date = CharField(max_length=100,
                          required=True,
                          widget=TextInput())
    born_location = CharField(max_length=100,
                              required=True,
                              widget=TextInput())
    description = CharField(
        required=True,
        widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
