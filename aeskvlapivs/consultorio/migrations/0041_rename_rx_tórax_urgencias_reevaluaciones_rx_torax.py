# Generated by Django 4.1.1 on 2022-09-13 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0040_urgencias_reevaluaciones_pit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urgencias_reevaluaciones',
            old_name='Rx_Tórax',
            new_name='Rx_Torax',
        ),
    ]
