from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #================Jabatan=====================#
    path('jabatan/', views.jabatan, name='jabatan'),
    path('tambah_jabatan', views.tambah_jabatan, name='tambah_jabatan'),
    path('edit_jabatan/<int:id>', views.edit_jabatan, name='edit_jabatan'),
    path('hapus_jabatan/<int:id>', views.hapus_jabatan, name='hapus_jabatan'),

    #================Pendidikan=====================#
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('tambah_pendidikan', views.tambah_pendidikan, name='tambah_pendidikan'),
    path('edit_pendidikan/<int:id>', views.edit_pendidikan, name='edit_pendidikan'),
    path('hapus_pendidikan/<int:id>',
         views.hapus_pendidikan, name='hapus_pendidikan'),

    #================desa=====================#
    path('desa/', views.desa, name='desa'),
    path('tambah_desa', views.tambah_desa, name='tambah_desa'),
    path('edit_desa/<int:id>', views.edit_desa, name='edit_desa'),
    path('hapus_desa/<int:id>', views.hapus_desa, name='hapus_desa'),


    #================Kecamatan=====================#
    path('kecamatan/', views.kecamatan, name='kecamatan'),
    path('tambah_kecamatan', views.tambah_kecamatan, name='tambah_kecamatan'),
    path('edit_kecamatan/<int:id>', views.edit_kecamatan, name='edit_kecamatan'),
    path('hapus_kecamatan/<int:id>', views.hapus_kecamatan, name='hapus_kecamatan'),

    #================Kabupaten=====================#
    path('kabupaten/', views.kabupaten, name='kabupaten'),
    path('tambah_kabupaten', views.tambah_kabupaten, name='tambah_kabupaten'),
    path('edit_kabupaten/<int:id>', views.edit_kabupaten, name='edit_kabupaten'),
    path('hapus_kabupaten/<int:id>', views.hapus_kabupaten, name='hapus_kabupaten'),

    #===================Enrol====================#
    path('enrol/', views.enrol, name='enrol'),
    path('daftar', views.daftar, name='daftar'),
    path('latih', views.latih, name='latih'),
    path('detect', views.detect, name='detect'),

    #===================Guru==============#
    path('guru/', views.guru, name='guru'),
    path('tambah_guru', views.tambah_guru, name='tambah_guru'),
    path('edit_guru/<int:id>', views.edit_guru, name='edit_guru'),
    path('hapus_guru/<int:id>', views.hapus_guru, name='hapus_guru'),

    #=====================Absensi===================#
    path('absensi/', views.absensi, name='absensi'),
    path('tambah_absensi', views.tambah_absensi, name='tambah_absensi'),
    path('edit_absensi/<int:id>', views.edit_absensi, name='edit_absensi'),
    path('hapus_absensi/<int:id>', views.hapus_absensi, name='hapus_absensi'),

    #=====================Laporan===================#
    path('laporan/', views.laporan, name='laporan'),
    # path('print', views.print, name='print'),
    path('pdf', views.pdf, name='pdf'),

    #===============login logout=====================#
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='home'), name='keluar'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
