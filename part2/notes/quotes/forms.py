from django.forms import ModelForm, CharField, Textarea
from .models import Quote


class QuoteForm(ModelForm):
    quote = CharField(max_length=100,
                      required=True,
                      widget=Textarea(attrs={'rows': 5, 'cols': 50}))
    author_fullname = CharField()  # Add this line
    tags = CharField(max_length=100)
    # Add this line

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author_fullname']
