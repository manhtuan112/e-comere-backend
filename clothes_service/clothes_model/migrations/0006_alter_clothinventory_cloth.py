# Generated by Django 4.1.7 on 2023-06-08 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_model', '0005_alter_clothinventory_cloth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothinventory',
            name='cloth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='clothes_model.cloth'),
        ),
    ]
