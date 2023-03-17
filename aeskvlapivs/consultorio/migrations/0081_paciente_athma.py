# Generated by Django 4.1.7 on 2023-03-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0080_urgencias_esp_otro_urgencias_especialidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='athma',
            field=models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Asma'),
        ),
    ]