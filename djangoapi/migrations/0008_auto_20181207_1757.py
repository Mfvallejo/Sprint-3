# Generated by Django 2.1.4 on 2018-12-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0007_auto_20181115_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espaciomodel',
            name='parqueadero',
        ),
        migrations.AddField(
            model_name='parqueaderomodel',
            name='nombre',
            field=models.CharField(default='manuel', max_length=100),
            preserve_default=False,
        ),
    ]