# Generated by Django 3.1.1 on 2021-05-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20210516_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='46c588ce0d9d517f9fc1', editable=False, max_length=20),
        ),
    ]
