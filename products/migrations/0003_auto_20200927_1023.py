# Generated by Django 3.1.1 on 2020-09-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200927_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmproduct',
            name='prod_name',
            field=models.CharField(max_length=100),
        ),
    ]
