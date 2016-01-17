# encoding: utf-8

from django.http import Http404
from django.shortcuts import render



def Home (request):
	return render(request,'home.html')
