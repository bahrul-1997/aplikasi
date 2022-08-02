# Generated by Django 4.0.6 on 2022-07-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0003_mguru'),
    ]

    operations = [
        migrations.AddField(
            model_name='mguru',
            name='foto',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='mguru',
            name='desa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mdesa'),
        ),
        migrations.AlterField(
            model_name='mguru',
            name='jabatan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mjabatan'),
        ),
        migrations.AlterField(
            model_name='mguru',
            name='kabupaten',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mkabupaten'),
        ),
        migrations.AlterField(
            model_name='mguru',
            name='kecamatan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mkecamatan'),
        ),
        migrations.AlterField(
            model_name='mguru',
            name='pendidikan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='absensi.mpendidikan'),
        ),
    ]
