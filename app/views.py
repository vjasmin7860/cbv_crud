from django.shortcuts import render
from django.views .generic import ListView,DetailView
from app.models import *
from django.http import HttpResponse
# Create your views here.


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