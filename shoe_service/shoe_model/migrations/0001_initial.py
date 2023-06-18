# Generated by Django 4.1.7 on 2023-06-08 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(default=None, max_length=1000, null=True)),
                ('category', models.CharField(default=None, max_length=1000, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(default=None, null=True)),
                ('color', models.CharField(default=None, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='clothes_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ShoeInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('shoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='shoe_model.shoe')),
            ],
        ),
    ]