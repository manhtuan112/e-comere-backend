# Generated by Django 4.1.7 on 2023-06-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product_type',
            field=models.CharField(default='Book', max_length=20),
        ),
    ]
