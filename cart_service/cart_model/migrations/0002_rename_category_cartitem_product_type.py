# Generated by Django 4.1.7 on 2023-06-08 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='category',
            new_name='product_type',
        ),
    ]