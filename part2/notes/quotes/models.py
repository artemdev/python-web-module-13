from django.db import models
from authors.models import Author


class Quote(models.Model):
    quote = models.CharField(max_length=100, null=False)
    tags = models.CharField(max_length=100, null=False)  # Use ListField
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='quotes', default=1)
