# Generated by Django 4.1.7 on 2023-06-07 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_model', '0002_remove_inventory_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='inventory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes_model.inventory'),
        ),
    ]
