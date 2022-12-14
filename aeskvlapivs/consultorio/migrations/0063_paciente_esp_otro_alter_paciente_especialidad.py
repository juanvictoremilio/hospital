# Generated by Django 4.1.1 on 2022-09-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0062_paciente_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='esp_otro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Especifique otro'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='especialidad',
            field=models.CharField(blank=True, choices=[('Medicina General', 'Medicina General'), ('Urgenciasas', 'Urgencias'), ('Medicina Interna', 'Medicina Interna'), ('Intensivista', 'Intensivista'), ('Cirugía', 'Cirugía'), ('Cardiología', 'Cardiología'), ('Neurología', 'Neurología'), ('Neurocirugía', 'Neurocirugía'), ('Ortopedia', 'Ortopedia'), ('Ginecología', 'Ginecología'), ('Gastroenterología', 'Gastroenterología'), ('Nefrología', 'Nefrología'), ('Otro', 'Otro')], max_length=20, null=True),
        ),
    ]
