'''
Created on 19/07/2011

@author: lesthack
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
 
def new(request):
    return render_to_response('new.html', {})

def list(request):
    codes = [i for i in range(10)]
    return render_to_response('list.html', locals())

def code(request, name):
    code = name.split(".")
    return render_to_response('code.html', {"name":code[0], "extension":code[1]})