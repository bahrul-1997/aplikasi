import os
import cv2
from django.conf import settings
import numpy as np
from PIL import Image
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required

from xhtml2pdf import pisa
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template


def home(request):
    context = {
        'judul': 'Halaman Utama'
    }
    return render(request, 'absensi/Halaman_utama.html', context)


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    guru = Mguru.objects.all().count
    absen = Mabsen.objects.all().count
    hadir = Mabsen.objects.filter(keterangan=('Hadir')).count
    izin = Mabsen.objects.filter(keterangan=('Izin')).count
    context = {
        'guru': guru,
        'absen': absen,
        'hadir': hadir,
        'izin': izin,
        'judul': 'Halaman Data Dashboard'
    }
    return render(request, 'absensi/dashboard.html', context)

#=======================Jabatan====================#


@login_required(login_url=settings.LOGIN_URL)
def jabatan(request):
    tampil = Mjabatan.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Jabatan'
    }
    return render(request, 'absensi/jabatan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_jabatan(request):
    if request.POST:
        form = Fjabatan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    else:
        form = Fjabatan()
        konteks = {
            'form': form,
            'judul': "Halaman Tambah Jabatan"
        }

    return render(request, 'tambah/jabatan.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def edit_jabatan(request, id):
    form = Fjabatan(instance=Mjabatan.objects.get(id=id))
    context = {
        'form': form,
        'judul': 'Tambah Data Jabatan'
    }
    return render(request, 'edit/jabatan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def edit_jabatan(request, id):
    jabatan = Mjabatan.objects.get(id=id)
    template = 'edit/jabatan.html'
    if request.POST:
        form = Fjabatan(request.POST, request.FILES, instance=jabatan)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    else:
        form = Fjabatan(instance=jabatan)
        konteks = {
            'form': form,
            'jabatan': jabatan,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_jabatan(request, id):
    Mjabatan.objects.get(id=id).delete()
    return redirect('jabatan')

#======================END Jabatan=====================#

#=================Pendidikan======================#


@login_required(login_url=settings.LOGIN_URL)
def pendidikan(request):
    tampil = Mpendidikan.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Pendidikan'
    }
    return render(request, 'absensi/pendidikan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_pendidikan(request):
    if request.POST:
        form = Fpendidikan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pendidikan')
    else:
        form = Fpendidikan()
        konteks = {
            'form': form,
            'judul': "Halaman Tambah Pendidikan"
        }

    return render(request, 'tambah/pendidikan.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def edit_pendidikan(request, id):
    pendidikan = Mpendidikan.objects.get(id=id)
    template = 'edit/pendidikan.html'
    if request.POST:
        form = Fpendidikan(request.POST, request.FILES, instance=pendidikan)
        if form.is_valid():
            form.save()
            return redirect('pendidikan')
    else:
        form = Fpendidikan(instance=pendidikan)
        konteks = {
            'form': form,
            'pendidikan': pendidikan,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_pendidikan(request, id):
    Mpendidikan.objects.get(id=id).delete()
    return redirect('pendidikan')
#======================End Pendidikan=============#

#=============================Desa=======================#


@login_required(login_url=settings.LOGIN_URL)
def desa(request):
    tampil = Mdesa.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Desa'
    }
    return render(request, 'absensi/desa.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_desa(request):
    if request.POST:
        form = Fdesa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desa')
    else:
        form = Fdesa()
        konteks = {
            'form': form,
            'judul': "Halaman Tambah Desa"
        }

    return render(request, 'tambah/desa.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def edit_desa(request, id):
    desa = Mdesa.objects.get(id=id)
    template = 'edit/desa.html'
    if request.POST:
        form = Fdesa(request.POST, request.FILES, instance=desa)
        if form.is_valid():
            form.save()
            return redirect('desa')
    else:
        form = Fdesa(instance=desa)
        konteks = {
            'form': form,
            'desa': desa,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_desa(request, id):
    Mdesa.objects.get(id=id).delete()
    return redirect('desa')
#=======================End Desa================#

#=========================Kecamatan============#


@login_required(login_url=settings.LOGIN_URL)
def kecamatan(request):
    tampil = Mkecamatan.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Kecamatan'
    }
    return render(request, 'absensi/kecamatan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_kecamatan(request):
    if request.POST:
        form = Fkecamatan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kecamatan')
    else:
        form = Fkecamatan()
        konteks = {
            'form': form,
            'judul': "Halaman Tambah Kecamatan"
        }

    return render(request, 'tambah/kecamatan.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def edit_kecamatan(request, id):
    kecamatan = Mkecamatan.objects.get(id=id)
    template = 'edit/kecamatan.html'
    if request.POST:
        form = Fkecamatan(request.POST, request.FILES, instance=kecamatan)
        if form.is_valid():
            form.save()
            return redirect('kecamatan')
    else:
        form = Fkecamatan(instance=kecamatan)
        konteks = {
            'form': form,
            'kecamatan': kecamatan,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_kecamatan(request, id):
    Mkecamatan.objects.get(id=id).delete()
    return redirect('kecamatan')
#======================End Kecamatan=================#

#=======================Kabupaten============#


@login_required(login_url=settings.LOGIN_URL)
def kabupaten(request):
    tampil = Mkabupaten.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Kabupaten'
    }
    return render(request, 'absensi/kabupaten.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_kabupaten(request):
    if request.POST:
        form = Fkabupaten(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kabupaten')
    else:
        form = Fkabupaten()
        konteks = {
            'form': form,
            'judul': "Halaman Tambah Kabupaten"
        }

    return render(request, 'tambah/kabupaten.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def edit_kabupaten(request, id):
    kabupaten = Mkabupaten.objects.get(id=id)
    template = 'edit/kabupaten.html'
    if request.POST:
        form = Fkabupaten(request.POST, request.FILES, instance=kabupaten)
        if form.is_valid():
            form.save()
            return redirect('kabupaten')
    else:
        form = Fkabupaten(instance=kabupaten)
        konteks = {
            'form': form,
            'kabupaten': kabupaten,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_kabupaten(request, id):
    Mkabupaten.objects.get(id=id).delete()
    return redirect('kabupaten')

#=====================End Kabupaten=================#

#====================Guru============================#


@login_required(login_url=settings.LOGIN_URL)
def guru(request):
    tampil = Mguru.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Guru'
    }
    return render(request, 'absensi/guru.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_guru(request):
    if request.POST:
        form = Fguru(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guru')
        else:
            return redirect('tambah_guru')
    else:
        form = Fguru()
        context = {
            'form': form,
            'judul': "Halaman Tambah Guru"
        }
    return render(request, 'tambah/guru.html', context)


@login_required(login_url=settings.LOGIN_URL)
def edit_guru(request, id):
    guru = Mguru.objects.get(id=id)
    template = 'edit/guru.html'
    if request.POST:
        form = Fguru(request.POST, request.FILES, instance=guru)
        if form.is_valid():
            form.save()
            return redirect('guru')
    else:
        form = Fguru(instance=guru)
        konteks = {
            'form': form,
            'guru': guru,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_guru(request, id):
    Mguru.objects.get(id=id).delete()
    return redirect('guru')

#=================END Guru===========================#

#=================Enrol=============================#


@login_required(login_url=settings.LOGIN_URL)
def enrol(request):
    form = Fabsen()

    context = {
        'form': form,
        'judul': 'Halaman Pendaftaran Wajah'
    }
    return render(request, 'absensi/enrol.html', context)


@login_required(login_url=settings.LOGIN_URL)
def daftar(request):
    if request.method == "POST":
        face_id = int(request.POST['guru'])
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)
        face_detector = cv2.CascadeClassifier(
            'ml/haarcascade_frontalface_default.xml')
        print("[INFO] Initializing face capture. Look the camera and wait ...")
        count = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 1:
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    count += 1
                    cv2.imwrite("ml/dataset/User." + str(face_id) + '.' +
                                str(count) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.waitKey(250)

                cv2.imshow('Daftar', img)
                k = cv2.waitKey(1) & 0xff
                if k == 27:
                    break
                elif count >= 30:
                    break
                print(count)
            else:
                print("\n multiple faces detected")

        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
    else:
        print("Its a GET method.")

    return redirect('enrol')


@login_required(login_url=settings.LOGIN_URL)
def latih(request):

    path = 'ml/dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("ml/haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faceSamples.append(img_numpy)
            ids.append(id)
            cv2.imshow("training", img_numpy)
            cv2.waitKey(10)
        return np.array(faceSamples), np.array(ids)

    print("[INFO] Training faces. It will take a few seconds. Wait ...")

    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, ids)
    recognizer.save('ml/recognizer/latih.yml')
    print("[INFO] {0} faces trained. Exiting Program".format(
        len(np.unique(ids))))
    cv2.destroyAllWindows()

    request, "{0} faces trained successfully".format(len(np.unique(ids)))

    return redirect('enrol')

#====================End Enrol======================#
#====================Absensi========================#


@login_required(login_url=settings.LOGIN_URL)
def absensi(request):
    tampil = Mabsen.objects.all()
    context = {
        'tampil': tampil,
        'judul': 'Halaman Data Absensi'
    }
    return render(request, 'absensi/absensi.html', context)


@login_required(login_url=settings.LOGIN_URL)
def tambah_absensi(request):
    if request.POST:
        form = Fabsen1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('absensi')
        else:
            return redirect('tambah_absensi')
    else:
        form = Fabsen1()
        context = {
            'form': form,
            'judul': "Halaman Absen Manual"
        }
    return render(request, 'tambah/absensi.html', context)


@login_required(login_url=settings.LOGIN_URL)
def edit_absensi(request, id):
    absen = Mabsen.objects.get(id=id)
    template = 'edit/absensi.html'
    if request.POST:
        form = Fabsen1(request.POST, instance=absen)
        if form.is_valid():
            form.save()
            return redirect('absensi')
    else:
        form = Fabsen1(instance=absen)
        konteks = {
            'form': form,
            'absensi': absen,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_absensi(request, id):
    Mabsen.objects.get(id=id).delete()
    return redirect('absensi')
#=====================End Absensi========================#

#======================Laporan========================#


@login_required(login_url=settings.LOGIN_URL)
def laporan(request):
    tampil = Mabsen.objects.all().order_by('-id')
    context = {
        'tampil': tampil,
        'judul': 'Semua Data Laporan'
    }
    return render(request, 'absensi/laporan.html', context)


def pdf(request):
    if request.POST:
        date1 = request.POST.get('awal')
        date2 = request.POST.get('ahir')
        lapor1 = Mabsen.objects.filter(jam_masuk__range=[date1, date2])
        print(lapor1)
        template_path = 'absensi/pdf_template.html'
        context = {'laporan': lapor1}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="laporan' + \
            str(date1) + 'sampai' + str(date2)+'.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    else:
        lapor1 = Mabsen.objects.all()
        print(lapor1)
        template_path = 'absensi/pdf_template.html'
        context = {'laporan': lapor1}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="report.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


def detect(request):
    faceDetect = cv2.CascadeClassifier(
        'ml/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read('ml/recognizer/latih.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # This will predict the id of the face
            getId, conf = rec.predict(gray[y:y + h, x:x + w])
            print(getId, conf)
            confidence = "  {0}%".format(round(100 - conf))
            # print conf;
            if conf < 35:
                try:
                    user = Mguru.objects.get(id=getId)
                except Mguru.DoesNotExist:
                    pass

                print("User Name", user.nama)

                userId = getId
                if user.nama:
                    cv2.putText(img, user.nama, (x+5, y+h-10),
                                font, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "Detected", (x, y + h),
                                font, 1, (0, 255, 0), 2)
            else:
                cv2.putText(img, "Wajah Tidak Di Kenali",
                            (x, y + h), font, 1, (0, 0, 255), 2)

            cv2.putText(img, str(confidence), (x + 5, y - 5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow("Deteksi", img)
        if (cv2.waitKey(1) == ord('q')):
            break
        elif (userId != 0):
            absen = Mabsen()
            absen.guru = Mguru.objects.get(id=user.id)
            absen.keterangan = 'Hadir'
            absen.save()
            cv2.waitKey(2000)
            cam.release()
            cv2.destroyAllWindows()
            return redirect('/')

    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')
