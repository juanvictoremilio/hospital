# Generated by Django 4.0.5 on 2022-06-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0004_alter_reevaluacion_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reevaluacion',
            name='climc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Clasificación Masa Corporal'),
        ),
    ]
