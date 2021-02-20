# Generated by Django 3.1.6 on 2021-02-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndaluciaCOVID_Dashboard', '0017_auto_20210214_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicdistrit',
            name='confirmed14100hab',
            field=models.DecimalField(decimal_places=20, max_digits=30, verbose_name='Confirmados 14 días x 100.000 hab'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='confirmed14100hab',
            field=models.DecimalField(decimal_places=20, max_digits=30, verbose_name='Confirmados 14 días x 100.000 hab'),
        ),
    ]