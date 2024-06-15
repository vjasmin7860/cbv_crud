from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from app.models import *
from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(scname='svs') --> here it will  give particular school names
    #ordering=['scname']--> here it will give the alphabetical order


def wish(request,n):
    return HttpResponse(f'hi {n} how are you')

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'