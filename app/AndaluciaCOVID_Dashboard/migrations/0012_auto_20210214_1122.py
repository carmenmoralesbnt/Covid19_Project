# Generated by Django 3.1.6 on 2021-02-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndaluciaCOVID_Dashboard', '0011_auto_20210214_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historictownship',
            name='Confirmados_PCR_TA_14d',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='confirmed14100hab',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]