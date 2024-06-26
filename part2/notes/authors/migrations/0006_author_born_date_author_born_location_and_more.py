# Generated by Django 5.0.4 on 2024-05-01 21:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_rename_name_author_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='born_date',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='born_location',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
