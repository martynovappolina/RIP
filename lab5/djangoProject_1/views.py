from datetime import date

from django.shortcuts import render

# Create your views here.
#def GetTheatres(request):
    #return render(request, 'theatres.html', {'data': {
     #   'theatres': [
      #      {'title': 'Большой театр', 'id': 1},
       #     {'title': 'Театр Ленком', 'id': 2},
        #    {'title': 'Театр Сатиры', 'id': 3},
        #]
    #}})

#def GetTheatre(request, id):
 #   return render(request, 'theatre.html', {'data': {
  #      'id': id
   # }})
from djangoProject_1.models import Theatre

def theatreList(request):
    return render(request, 'theatres.html', {'data': {
        'current_date': date.today(),
        'theatres': Theatre.objects.all()
    }})

def GetTheatre(request, id):
    return render(request, 'theatre.html', {'data' : {
        'current_date': date.today(),
        'theatre': Theatre.objects.filter(id=id)[0]
    }})
