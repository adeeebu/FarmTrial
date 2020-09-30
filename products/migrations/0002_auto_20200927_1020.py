# Generated by Django 3.1.1 on 2020-09-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.IntegerField()),
                ('prod_type', models.CharField(max_length=50)),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_price', models.FloatField()),
                ('prod_brand', models.CharField(max_length=50)),
                ('prod_link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='FarmProducts',
        ),
    ]
