# Generated by Django 5.0.1 on 2024-06-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XBOX', '0002_category_hidden_product_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
