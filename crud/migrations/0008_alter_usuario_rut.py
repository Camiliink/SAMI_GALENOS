# Generated by Django 5.0.6 on 2024-11-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_alter_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(db_index=True, max_length=12),
        ),
    ]
