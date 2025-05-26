from django.shortcuts import render

def add_client(request):
    context = {}
    return render(request, 'client/addclient.html', context)
def one_client(request, id):
    context = {}
    return render(request, 'client/oneclient.html',context )

def all_clients(request):
    context = {}
    return render(request, 'client/allclients.html', context)