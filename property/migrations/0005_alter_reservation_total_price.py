# Generated by Django 5.0.3 on 2024-05-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_favorited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='total_price',
            field=models.FloatField(),
        ),
    ]