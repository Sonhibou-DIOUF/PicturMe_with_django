from django.shortcuts import render
from .forms import PhotographerForm, PhotographerModelForm
from photographer.models import Photographer
# Create your views here.
def add_photographer(request):
    """
       Add a photographer
    """
    if request.method == 'POST':
        form = PhotographerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PhotographerModelForm()
    context={'form':form}
    return render(request, 'photographer/addphotographer.html', context)

def one_photographer(request, id):
    context = {}
    return render(request, 'photographer/onephotographer.html', context)


def all_photographers(request):
    context = {}
    return render(request, 'photographer/allphotographers.html', context)
