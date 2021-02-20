# Generated by Django 3.1.6 on 2021-02-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndaluciaCOVID_Dashboard', '0014_auto_20210214_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Distritos'},
        ),
        migrations.AlterModelOptions(
            name='historicdistrit',
            options={'verbose_name': 'Histórico de datos por distrito sanitario'},
        ),
        migrations.AlterModelOptions(
            name='historicprovince',
            options={'verbose_name': 'Histórico de datos por Provincia'},
        ),
        migrations.AlterModelOptions(
            name='historictownship',
            options={'verbose_name': 'Histórico de datos por municipio'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': 'Provincias'},
        ),
        migrations.AlterModelOptions(
            name='township',
            options={'verbose_name': 'Municipios'},
        ),
        migrations.AlterField(
            model_name='historicdistrit',
            name='deceases',
            field=models.IntegerField(verbose_name='Fallecidos'),
        ),
        migrations.AlterField(
            model_name='historicdistrit',
            name='totalConfirmed',
            field=models.IntegerField(verbose_name='Confirmados totales'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='Confirmados_PCR_TA',
            field=models.IntegerField(verbose_name='Confirmados por PCR TOTAL'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='Confirmados_PCR_TA_14d',
            field=models.IntegerField(verbose_name='Confirmados PCR 14 días'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='confirmed14100hab',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Confirmados 14 días x 100.000 hab'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='deceases',
            field=models.IntegerField(verbose_name='Fallecidos'),
        ),
        migrations.AlterField(
            model_name='historictownship',
            name='totalConfirmed',
            field=models.IntegerField(verbose_name='Confirmados totales'),
        ),
        migrations.AlterUniqueTogether(
            name='historicdistrit',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='historicprovince',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='historictownship',
            unique_together=set(),
        ),
    ]