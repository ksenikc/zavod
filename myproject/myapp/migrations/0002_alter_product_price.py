# Generated by Django 4.2 on 2024-11-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=120, verbose_name='Цена'),
        ),
    ]
