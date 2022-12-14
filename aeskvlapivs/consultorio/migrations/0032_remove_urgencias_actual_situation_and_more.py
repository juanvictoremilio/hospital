# Generated by Django 4.0.6 on 2022-09-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0031_urgencias_actual_situation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urgencias',
            name='actual_situation',
        ),
        migrations.AddField(
            model_name='urgencias',
            name='OBSERVACIONES_GENERALES',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias',
            name='AVPU',
            field=models.CharField(blank=True, choices=[('Alerta', 'A Alerta'), ('Respuesta Verbal', 'V Respuesta Verbal'), ('Respuesta al Dolor', 'P Respuesta al Dolor'), ('Sin Respuesta', 'U Sin Respuesta')], max_length=50, null=True, verbose_name='Estado de Conciencia'),
        ),
        migrations.AlterField(
            model_name='urgencias',
            name='Respuesta_Motora',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=1, help_text='Obedece órdenes 6, Localiza dolor 5, Retirada al dolor 4, Flexión anormal 3, Extensión anormal 2, Ausencia de Respuesta 1', null=True),
        ),
        migrations.AlterField(
            model_name='urgencias',
            name='Respuesta_Verbal',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=1, help_text='Orientado 5, Desorientado confuso 4, Incoherente 3, Sonidos incomprensibles 1.', null=True),
        ),
        migrations.AlterField(
            model_name='urgencias',
            name='apertura_ocular',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=1, help_text='Espontánea 4, Orden verbal 3, Est. Doloroso 2. No Apertura 1.', null=True),
        ),
    ]
