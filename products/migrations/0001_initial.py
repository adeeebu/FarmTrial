# Generated by Django 3.1.1 on 2020-09-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.IntegerField()),
                ('prod_type', models.CharField(max_length=50)),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_price', models.FloatField()),
                ('prod_brand', models.CharField(max_length=50)),
            ],
        ),
    ]
