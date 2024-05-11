from django.db import models


class Author(models.Model):
    fullname = models.CharField(null=False, unique=True)
    born_date = models.CharField(null=False)
    born_location = models.CharField(null=False)
    description = models.CharField(null=False)
