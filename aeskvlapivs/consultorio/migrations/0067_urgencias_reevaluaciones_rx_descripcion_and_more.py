# Generated by Django 4.1.1 on 2022-10-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0066_alter_urgencias_reevaluaciones_pafi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Rx_descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripciones Radiológicas'),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='FrIO2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.21, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='RASS',
            field=models.CharField(blank=True, choices=[('+4 Combativo', 'RASS +4 Combativo'), ('+3 Muy agitado', 'RASS +3 Muy agitado'), ('+2 agitado', 'RASS +2 Agitado'), ('+1 inquieto', 'RASS +1 Inquieto'), ('0 Despierto y Tranquilo', 'RASS 0 Despierto y tranuilo'), ('-1 somnoliento', 'RASS -1 Somnoliento'), ('-2 sedación leve', 'RASS -2 Sedación leve'), ('-3 sedación moderada', 'RASS -3 Sedación moderada'), ('RASS -4 sedación profunda', 'RASS -4 Sedación profunda'), ('-5 sin respuesta', 'RASS -5 Sin respuesta')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='mode',
            field=models.CharField(blank=True, choices=[('Mode VAC', 'Mode VAC'), ('Mode PAC', 'Mode PAC'), ('ModeVSIMC', 'Mode VSIMC'), ('Mode PSIMC', 'Mode PSIMC'), ('Mode Psup', 'Mode Psup')], max_length=15, null=True, verbose_name='Modo Ventilatorio'),
        ),
    ]
