# Generated by Django 4.1.1 on 2023-02-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0072_paciente_medications_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='evaluacion_sec',
            field=models.CharField(blank=True, choices=[('Segunda Evaluación', 'Segunda Evaluación'), ('Tercera Evaluación', 'Tercera Evaluación'), ('Cuarta Evaluación', 'Cuarta Evaluación'), ('Quinta Evaluación', 'Quinta Evaluación'), ('Sexta Evaluación', 'Sexta Evaluación'), ('Séptima Evaluación', 'Séptima Evaluación'), ('Octava Evaluación', 'Octava Evaluación')], max_length=50, null=True, verbose_name='Evaluación Subsecuente'),
        ),
    ]
