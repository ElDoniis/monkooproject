from django.http import QueryDict
from django.shortcuts import render
from monkoo_calendar.models import Events
import json

def toListValues(eventToList):
    values = []
    posIni = eventToList.find('"title":')
    posFinal = eventToList.find('"start"')
    value = eventToList[posIni+8:posFinal-1]
    value = value.strip('\\n"')
    values.append(value)

    posIni = eventToList.find('"start":')
    posFinal = eventToList.find('"end"')
    value = eventToList[posIni+8:posFinal-1]
    value = value.strip('"')
    values.append(value)

    posIni = eventToList.find('"end":')
    posFinal = eventToList.find('"backgroundColor"')
    value = eventToList[posIni+6:posFinal-1]
    value = value.strip('"')
    values.append(value)

    posIni = eventToList.find('"backgroundColor":')
    posFinal = eventToList.find('"borderColor"')
    value = eventToList[posIni+18:posFinal-1]
    value = value.strip('"')
    values.append(value)
    values.append(value)
    return values

def send_events(request):
    if request.method == 'POST':
        formaEvento = request.POST
        formaEvento = QueryDict.dict(formaEvento)

        # Los eventos cuando se traen quedan en un unico string por lo que hay que separar el string por eventos
        # Convertir data traida en diccionario - sanear data -
        x = formaEvento['dataEventos'].count('}')
        izq = 0
        calendarEventsValues = None
        memory = Events.objects.all()
        memorySize = Events.objects.count()

        for i in range(x):
            der = formaEvento['dataEventos'].find('}', izq)
            singleEvent = formaEvento['dataEventos'][izq:der+1]
            calendarEventsValues = toListValues(singleEvent)
            event = Events()
            # Si el evento ya existe no lo guarda
            if Events.objects.filter(userId=request.user.id, title=calendarEventsValues[0], start=calendarEventsValues[1],
            end=calendarEventsValues[2], backgroundColor=calendarEventsValues[3], borderColor=calendarEventsValues[4]).exists():
                pass
            else:
                print('hola')
                event.userId = request.user.id
                event.title = calendarEventsValues[0]
                event.start = calendarEventsValues[1]
                event.end = calendarEventsValues[2]
                event.backgroundColor = calendarEventsValues[3]
                event.borderColor = calendarEventsValues[4]            
                event.save()
            izq = der+2

    if request.user.is_authenticated:
        print(f"Username --> {request.user.username}")
        print(f"Username --> {request.user.id}")

    # Traer eventos que se encuentrar en la database
    query_set = Events.objects.filter(userId = request.user.id)
    first_convertion = query_set.values()
    all_events = list(first_convertion)
    context = {'data': json.dumps (all_events)}
    return render(request, 'home/calendar.html', context)

def recomendacionParis(request):
    return render(request, 'home/recomendacionParis.html')

def recomendacionJapon(request):
    return render(request, 'home/recomendacionJapon.html')

def recomendacionVietnam(request):
    return render(request, 'home/recomendacionVietnam.html')
