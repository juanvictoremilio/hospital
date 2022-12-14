# Generated by Django 4.1.1 on 2022-09-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0046_urgencias_reevaluaciones_dxs'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Labs1',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Labs2',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Labs3',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Labs4',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='Labs5',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image1',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image10',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image2',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image3',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image4',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image5',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image6',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image7',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image8',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='image9',
            field=models.FileField(blank=True, help_text='formato pdf, jpg, jpge', null=True, upload_to='Urgencias_EvSecs'),
        ),
        migrations.AddField(
            model_name='urgencias_reevaluaciones',
            name='pO2',
            field=models.PositiveSmallIntegerField(blank=True, help_text='mm/Hg', null=True, verbose_name='pO2'),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='O2',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='En litros/min', null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='dxs',
            field=models.TextField(blank=True, null=True, verbose_name='CONFIRMACION O REESTRUCTURACION DIAGNOSTICA'),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='interconsulta',
            field=models.CharField(blank=True, choices=[('Medicina Interna', 'Medicina Interna'), ('Cirug??a', 'Cirug??a'), ('Cardiolog??a', 'Cardiolog??a'), ('Neurolog??a', 'Neurolog??a'), ('Neurocirug??a', 'Neurocirug??a'), ('Ortopedia', 'Ortopedia'), ('Ginecolog??a', 'Ginecolog??a'), ('Gastroenterolog??a', 'Gastroenterolog??a'), ('Nefrolog??a', 'Nefrolog??a'), ('Otro', 'Otro')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='pCO2',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='mm/Hg', max_digits=5, null=True, verbose_name='pCo2'),
        ),
        migrations.AlterField(
            model_name='urgencias_reevaluaciones',
            name='sO2',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='sO2'),
        ),
    ]
