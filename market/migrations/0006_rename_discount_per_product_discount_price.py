# Generated by Django 4.1.1 on 2022-09-30 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_product_discount_per_delete_onsale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_per',
            new_name='discount_price',
        ),
    ]
