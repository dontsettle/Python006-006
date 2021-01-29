from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
###  从models取数据传给template  ###
from .models import Name

def week4(request):
    return HttpResponse('hello django!')
#  path('<int:year>', views.year), 
def year(request, year):
    return HttpResponse(year)
    # return redirect('/2020.html')

# # path('<int:year>/<str:name>', views.name),
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

# # path('<myint:year>', views.year), 
# # re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

def myyear(request, year):
    return render(request, 'yearview.html')

def books(request):
    #从models取数据传给template ###
    n = Name.objects.all()
    return render(request,'bookslist.html',locals())

   

