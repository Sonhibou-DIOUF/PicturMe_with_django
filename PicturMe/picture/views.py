from django.shortcuts import render

# Create your views here.
def add_picture(request):
    context = {}
    return render(request, 'picture/addpicture.html', context)

def one_picture(request, id):
    context = {}
    return render(request, 'picture/onepicture.html', context)

def all_pictures(request):
    context = {}
    return render(request, 'picture/allpictures.html', context)
