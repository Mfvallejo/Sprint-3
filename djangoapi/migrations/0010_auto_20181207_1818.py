# Generated by Django 2.1.4 on 2018-12-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0009_espaciomodel_parqueadero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamodel',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservamodel',
            name='fecha_inicio',
            field=models.DateField(auto_now_add=True),
        ),
    ]
