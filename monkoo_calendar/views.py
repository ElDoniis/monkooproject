from dataclasses import replace
from mimetypes import init
import re
from typing import final
from django.forms import modelform_factory
from django.http import QueryDict
from django.shortcuts import redirect, render
from monkoo_calendar.models import Events
import json

def send_events(request): 
    if request.method == 'POST':
        formaEvento = request.POST
        formaEvento = QueryDict.dict(formaEvento)
        # print(formaEvento["dataEventos"])
        for i in range(len(formaEvento['dataEventos'])):
            if formaEvento['dataEventos'][i] == ",":
                formaEvento['dataEventos'] = formaEvento['dataEventos'].replace(',', ' ')

        print (formaEvento['dataEventos'])

       
 
        

    query_set = Events.objects.all()
    first_convertion = query_set.values()
    all_events = list(first_convertion)

    context = {'data': json.dumps (all_events)}

    return render(request, 'home/calendar.html', context)
