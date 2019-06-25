from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'judul': 'predict'
    }
    return render(request, 'predict.html', context)
