# Generated by Django 4.1.7 on 2023-06-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='order_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]