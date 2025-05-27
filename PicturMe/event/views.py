from django.shortcuts import render
from .forms import EventForm, EventModelForm
from .models import Event
# Create your views here.
def add_event(request):
    """
        Add event
    """
    if request.method == 'POST':
        form = EventModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = EventModelForm()
    context = {'form': form}
    return render(request, 'event/addevent.html', context)
def one_event(request, id):
    context = {}
    return render(request, 'event/oneevent.html', context)

def all_events(request):
    context = {}
    return render(request, 'event/allevents.html', context)