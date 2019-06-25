from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .SVM import svm


def index(request):
    # print(request.POST)
    context = {
        'judul': 'Home',
    }
    if request.method == 'POST':
        context['post'] = request.POST
    else:
        context['post'] = 'masih belum ada yg disubmit jeh'
        return render(request, 'index.html', context)


def upload(request):
    context = {
        'kirim': False,
        'kirim1': False
    }
    fileTrain = ''
    file = ''
    if request.method == 'POST':
        if 'document' in request.FILES:
            file = request.FILES['document']
            fileTrain = file.name
            fs = FileSystemStorage()
            fileTrain = file.name
            if fs.exists(file.name):
                fs.delete(file.name)
            fs.save(file.name, file)
        elif 'document1' in request.FILES:
            file1 = request.FILES['document1']
            fileTrain = request.POST.get("namaFileTrain",'')
            print(fileTrain, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            fs = FileSystemStorage()
            if fs.exists(file1.name):
                fs.delete(file1.name)
            fs.save(file1.name, file1)

        data = svm.Classification_svm('media/%s' % fileTrain)

        result = data.classificationSVM()
        if 'document1' in request.FILES:
            hasil = data.predictUji('media/%s' % file1.name)
            context['data1'] = data.dataTest
            context['kirim1'] = True
            context['hasil'] = hasil
        # context['urlMediaPrediksi'] = fs.url(filename)
        context['file'] = file
        context['data'] = data.data
        context['namaFile'] = file
        context['kirim'] = True
        context['akurasi'] = result

    return render(request, 'index.html', context)


def accuracy(request, nama):
    context = {}
    data = svm.Classification_svm('media/%s' % nama)
    result = data.classificationSVM()
    context['result'] = result
    return render(request, 'accuracy.html', context)


def predict(request, nama):
    context = {
        'nama': nama,
        'kirim': False
    }
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        if fs.exists(file.name):
            fs.delete(file.name)
        fs.save(file.name, file)

        data = svm.Classification_svm('media/%s' % nama)
        result = data.predictUji('media/%s' % file.name)
        context['result'] = result
        context['data'] = data.dataTest
        context['rangeLenData'] = range(len(data.dataTest.values))
        context['lenColumn'] = len(data.dataTest.values[0])
        context['kirim'] = True

    return render(request, 'predict.html', context)
