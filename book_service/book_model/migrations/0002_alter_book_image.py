# Generated by Django 4.1.7 on 2023-05-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='book_images/'),
        ),
    ]