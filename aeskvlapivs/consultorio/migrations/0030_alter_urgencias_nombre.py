# Generated by Django 4.0.6 on 2022-09-04 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0029_alter_urgencias_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgencias',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente'),
        ),
    ]
