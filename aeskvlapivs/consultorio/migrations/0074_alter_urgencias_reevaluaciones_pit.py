# Generated by Django 4.1.1 on 2023-02-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0073_alter_urgencias_reevaluaciones_evaluacion_sec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='pit',
            field=models.CharField(blank=True, help_text='No escriba aquí, OJO: Son Kgs.', max_length=90, null=True, verbose_name='Presión Intratorácica Total'),
        ),
    ]
