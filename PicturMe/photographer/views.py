from django.shortcuts import render

# Create your views here.
def add_photographer(request):
    context = {}
    return render(request, 'photographer/addphotographer.html', context)

def one_photographer(request, id):
    context = {}
    return render(request, 'photographer/onephotographer.html', context)


def all_photographers(request):
    context = {}
    return render(request, 'photographer/allphotographers.html', context)
