from datetime import datetime
from tkinter import CASCADE, CURRENT
from django.db import models


class Mjabatan(models.Model):
    nama = models.CharField(max_length=100)
    ket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "jabatan"

    def __str__(self):
        return self.nama


class Mpendidikan(models.Model):
    nama = models.CharField(max_length=100)
    ket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "pendidikan"

    def __str__(self):
        return self.nama


class Mdesa(models.Model):
    nama = models.CharField(max_length=100)
    ket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "desa"

    def __str__(self):
        return self.nama


class Mkecamatan(models.Model):
    nama = models.CharField(max_length=100)
    ket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "kecamatan"

    def __str__(self):
        return self.nama


class Mkabupaten(models.Model):
    nama = models.CharField(max_length=100)
    ket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "kabupaten"

    def __str__(self):
        return self.nama


class Mguru(models.Model):
    jk = (
        ('laki-laki', 'laki-laki'),
        ('perempuan', 'perempuan'),
    )
    nip = models.IntegerField()
    nama = models.CharField(max_length=100)
    jabatan = models.ForeignKey(Mjabatan, on_delete=models.CASCADE, null=True)
    alamat = models.CharField(max_length=200)
    desa = models.ForeignKey(Mdesa, on_delete=models.CASCADE, null=True)
    kecamatan = models.ForeignKey(
        Mkecamatan, on_delete=models.CASCADE, null=True)
    kabupaten = models.ForeignKey(
        Mkabupaten, on_delete=models.CASCADE, null=True)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=100, null=True, choices=jk)
    pendidikan = models.ForeignKey(
        Mpendidikan, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(upload_to='upload/', null=True)

    class Meta:
        db_table = "guru"

    def __str__(self):
        return self.nama


class Mabsen(models.Model):
    ket = (
        ('Hadir', 'Hadir'),
        ('Alpa', 'Alpa'),
        ('Izin', 'Izin'),
        ('Sakit', 'Sakit'),
    )
    guru = models.ForeignKey(Mguru, on_delete=models.CASCADE, null=True)
    jam_masuk = models.DateTimeField(default=datetime.now)
    keterangan = models.CharField(max_length=100, null=True, choices=ket)

    class Meta:
        db_table = "absensi"
