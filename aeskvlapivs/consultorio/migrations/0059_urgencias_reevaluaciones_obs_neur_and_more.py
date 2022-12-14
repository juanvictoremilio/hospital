# Generated by Django 4.1.1 on 2022-09-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0058_paciente_fur_paciente_gestas_paciente_menarca_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='obs_neur',
            field=models.TextField(blank=True, null=True, verbose_name='Complemento observaciones Neurològicas'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Menarca',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='RASS',
            field=models.CharField(blank=True, choices=[('+4 Combativo', '+4 Combativo'), ('+3 Muy agitado', '+3 Muy agitado'), ('+2 agitado', '+2 Agitado'), ('+1 inquieto', '+1 Inquieto'), ('0 Despierto y Tranquilo', '0 Despierto y tranuilo'), ('-1 somnoliento', '-1 Somnoliento'), ('-2 sedación leve', '-2 Sedación leve'), ('-3 sedación moderada', '-3 Sedación moderada'), ('-4 sedación profunda', '-4 Sedación profunda'), ('-5 sin respuesta', '-5 Sin respuesta')], max_length=30, null=True),
        ),
    ]
