# Generated by Django 2.1.3 on 2018-11-15 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0002_auto_20181025_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espaciomodel',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='reservamodel',
            name='usuario',
        ),
    ]
