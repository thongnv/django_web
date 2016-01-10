from django.shortcuts import render
import datetime
from models import Dreamreal
from django.http import HttpResponse

# Create your views here.


def hello(request):
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    context = {'message': 'Hello', 'today': datetime.datetime.now().date(), 'day_of_week': daysOfWeek}
    return render(request, "hello.html", context)


def hello1(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def bye(request):
    text = """<h1>Good bye my love!</h1>"""
    return HttpResponse(text)


def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
      website="www.polo.com", mail="sorex@polo.com",
      name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name+"<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
      website="www.polo.com", mail="sorex@polo.com",
      name="sorex", phonenumber="002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)


def datamanipulation(request):
    res = ''

    #Filtering data:
    qs = Dreamreal.objects.filter(name = "paul")
    res += "Found : %s results<br>"%len(qs)

    #Ordering results
    qs = Dreamreal.objects.order_by("name")

    for elt in qs:
        res += elt.name + '<br>'

    return HttpResponse(res)
