# Generated by Django 5.0.4 on 2024-05-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_alter_author_born_date_alter_author_born_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=250),
        ),
    ]
