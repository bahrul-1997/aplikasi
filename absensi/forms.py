from django import forms
from .models import *


class Fjabatan(forms.ModelForm):
    class Meta:
        model = Mjabatan
        fields = "__all__"
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan Nama Jabatan'}),
            'ket': forms.Textarea({'class': 'form-control',   'placeholder': 'Masukan Keterangan'})
        }


class Fpendidikan(forms.ModelForm):
    class Meta:
        model = Mpendidikan
        fields = "__all__"
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan Nama Pendidikan'}),
            'ket': forms.Textarea({'class': 'form-control',  'placeholder': 'Masukan Keterangan'})
        }


class Fdesa(forms.ModelForm):
    class Meta:
        model = Mdesa
        fields = "__all__"
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan Nama Desa'}),
            'ket': forms.Textarea({'class': 'form-control',  'placeholder': 'Masukan Keterangan'})
        }


class Fkecamatan(forms.ModelForm):
    class Meta:
        model = Mkecamatan
        fields = "__all__"
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan Nama Kecamatan'}),
            'ket': forms.Textarea({'class': 'form-control',  'placeholder': 'Masukan Keterangan'})
        }


class Fkabupaten(forms.ModelForm):
    class Meta:
        model = Mkabupaten
        fields = "__all__"
        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan Nama Kabupaten'}),
            'ket': forms.Textarea({'class': 'form-control',  'placeholder': 'Masukan Keterangan'})
        }


class Fguru(forms.ModelForm):
    class Meta:
        model = Mguru
        fields = "__all__"
        widgets = {
            'nip': forms.NumberInput({'class': 'form-control', 'autofocus': 'true', 'required': 'true', 'placeholder': 'Masukan NIP Guru'}),
            'nama': forms.TextInput({'class': 'form-control',  'required': 'true', 'placeholder': 'Masukan Nama Guru'}),
            'jabatan': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'alamat': forms.Textarea({'class': 'form-control',  'required': 'true', 'placeholder': 'Maasukan Nama Dusun', 'rows': '7'}),
            'desa': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'kecamatan': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'kabupaten': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'tgl_lahir': forms.DateInput({'class': 'form-control', 'type': 'date', 'required': 'true'}),
            'jenis_kelamin': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'pendidikan': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
        }


class Fabsen(forms.ModelForm):
    class Meta:
        model = Mabsen
        fields = ['guru']
        widgets = {
            'guru': forms.Select({'class': 'form-control chosen',  'required': 'true'}),

        }


class Fabsen1(forms.ModelForm):
    class Meta:
        model = Mabsen
        exclude = ['jam_masuk']
        widgets = {
            'guru': forms.Select({'class': 'form-control chosen',  'required': 'true'}),
            'keterangan': forms.Select({'class': 'form-control chosen',  'required': 'true'}),

        }
