# Generated by Django 4.0.6 on 2022-07-16 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0006_alter_mabsen_jam_masuk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mabsen',
            name='jam_masuk',
            field=models.DateTimeField(default=datetime.date(2022, 7, 17)),
        ),
    ]
