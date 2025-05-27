from django.shortcuts import render
from .forms import PictureModelForm, PictureForm
from .models import Picture
# Create your views here.
def add_picture(request):
    """
        Add a picture to the database
    """
    if request.method == 'POST':
        form = PictureModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PictureModelForm()
    context = {'form': form}
    return render(request, 'picture/addpicture.html', context)

def one_picture(request, id):
    context = {}
    return render(request, 'picture/onepicture.html', context)

def all_pictures(request):
    context = {}
    return render(request, 'picture/allpictures.html', context)
