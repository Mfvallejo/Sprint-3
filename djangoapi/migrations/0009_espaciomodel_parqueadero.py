# Generated by Django 2.1.4 on 2018-12-07 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0008_auto_20181207_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='espaciomodel',
            name='parqueadero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='djangoapi.ParqueaderoModel'),
        ),
    ]
