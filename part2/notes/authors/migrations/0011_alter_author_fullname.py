# Generated by Django 5.0.4 on 2024-05-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0010_alter_author_born_date_alter_author_born_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=55, unique=True),
        ),
    ]
