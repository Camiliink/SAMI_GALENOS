# Generated by Django 5.0.6 on 2024-11-22 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_centromedico_especialidad_medico_reservarcita'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecialidadMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(choices=[('cardiologia', 'Cardiología'), ('pediatria', 'Pediatría'), ('dermatologia', 'Dermatología')], max_length=50, verbose_name='Especialidad')),
                ('medico', models.ForeignKey(limit_choices_to={'tipo_usuario': 'medico'}, on_delete=django.db.models.deletion.CASCADE, to='crud.usuario', verbose_name='Médico')),
            ],
        ),
        migrations.DeleteModel(
            name='Especialidad_medico',
        ),
        migrations.AlterField(
            model_name='reservarcita',
            name='medico',
            field=models.ForeignKey(limit_choices_to={'tipo_usuario': 'medico'}, on_delete=django.db.models.deletion.CASCADE, to='crud.usuario', verbose_name='Médico'),
        ),
        migrations.AlterField(
            model_name='reservarcita',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.especialidadmedico', verbose_name='Especialidad'),
        ),
    ]
