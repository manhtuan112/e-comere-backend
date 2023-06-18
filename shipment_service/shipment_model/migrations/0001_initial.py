# Generated by Django 4.1.7 on 2023-06-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('shipment_status', models.CharField(default='Chờ lấy hàng', max_length=20)),
                ('order_id', models.IntegerField(default=1, max_length=10)),
                ('price', models.FloatField(default=1)),
            ],
        ),
    ]