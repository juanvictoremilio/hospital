# Generated by Django 4.1.1 on 2022-09-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0045_urgencias_reevaluaciones_pafi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='dxs',
            field=models.TextField(blank=True, null=True, verbose_name='CONDIRMACION O REESTRUCTURACION DIAGNOSTICA'),
        ),
    ]
