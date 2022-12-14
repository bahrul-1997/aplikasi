# Generated by Django 4.0.6 on 2022-07-16 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0004_mguru_foto_alter_mguru_desa_alter_mguru_jabatan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mabsen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jam_masuk', models.DateTimeField(auto_now_add=True)),
                ('keterangan', models.CharField(choices=[('Hadir', 'Hadir'), ('Alpa', 'Alpa'), ('Izin', 'Izin'), ('Sakit', 'Sakit')], max_length=100, null=True)),
                ('guru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mguru')),
            ],
            options={
                'db_table': 'absensi',
            },
        ),
    ]
