# encoding: utf-8

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from myproject.models import news_Main,carousel_Main


def mainController (request):
    news_entries = news_Main.objects.all()
    carousel_entries = carousel_Main.objects.all()
    return render_to_response('section/mainSection/main.html',context={'template_all_entries': news_entries,"carousel_entries":carousel_entries})

