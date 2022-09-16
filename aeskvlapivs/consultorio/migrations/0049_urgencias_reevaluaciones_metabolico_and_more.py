# Generated by Django 4.1.1 on 2022-09-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0048_alter_urgencias_reevaluaciones_po2'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='METABOLICO',
            field=models.CharField(blank=True, help_text='No escriba aquí', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='RASS',
            field=models.CharField(blank=True, choices=[('+4', '+4 Combativo'), ('+3', '+3 Muy agitado'), ('+2', '+2 Agitado'), ('+1', '+1'), ('-1', '-1 Somnoliento'), ('-2', '-2 Sedación leve'), ('-3', '-3 Sedación moderada'), ('-4', '-4 Sedación profunda'), ('-5', '-5 Sin respuesta')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Sedacion',
            field=models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='O2',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='En litros/min si es el caso', null=True),
        ),
    ]
