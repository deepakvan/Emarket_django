# Generated by Django 4.1.1 on 2022-09-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
