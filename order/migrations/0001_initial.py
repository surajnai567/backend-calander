# Generated by Django 3.1.1 on 2021-05-05 18:47

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('deliver', 'Delivered'), ('Pending', 'Pending'), ('On Way', 'On the Way'), ('Canceled', 'Canceled')], default='Pending', max_length=10)),
                ('totalamount', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('area', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=15)),
                ('itemquantity', models.CharField(max_length=10)),
                ('attribute', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=10)),
                ('itemImage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('itemprice', models.CharField(max_length=10)),
                ('itemtotal', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('total', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
