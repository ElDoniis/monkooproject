import re
from typing import final
from django.forms import modelform_factory
from django.shortcuts import redirect, render
from monkoo_calendar.models import Events
import json

def send_events(request): 
    query_set = Events.objects.all()
    first_convertion = query_set.values()
    all_events = list(first_convertion)

    context = {'data': json.dumps (all_events)}

    return render(request, 'home/calendar.html', context)

EventoForm = modelform_factory(Events, exclude=[])

def nuevo_evento(request):
    # recibir los datos
    if request.method == 'POST':
        formaEvento = EventoForm(request.POST)
        EventoForm.save()
        redirect('home/calendar.html')
    render(request, 'home/calendar.html', {"formaEvento": formaEvento})