from django.shortcuts import render

from client.forms import ClientModelForm


def add_client(request):
    """
        Add a Client
    """
    if request.method == 'POST':
        form = ClientModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ClientModelForm()
    context = {'form': form}
    return render(request, 'client/addclient.html', context)

def one_client(request, id):
    context = {}
    return render(request, 'client/oneclient.html',context )

def all_clients(request):
    context = {}
    return render(request, 'client/allclients.html', context)