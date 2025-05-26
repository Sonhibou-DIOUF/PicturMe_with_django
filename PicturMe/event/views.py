from django.shortcuts import render

# Create your views here.
def add_event(request):
    context = {}
    return render(request, 'event/addevent.html', context)
def one_event(request, id):
    context = {}
    return render(request, 'event/oneevent.html', context)

def all_events(request):
    context = {}
    return render(request, 'event/allevents.html', context)