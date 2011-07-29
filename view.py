'''
Created on 19/07/2011

@author: lesthack
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from pub.models import *
import datetime
 
lenguajes = {
        "C":"shBrushCpp.js",
        "C++":"shBrushCpp.js",
        "C#":"shBrushCSharp.js",
        "Css":"shBrushCss.js",
        "Delphi":"shBrushDelphi.js",
        "Java":"shBrushJava.js",
        "Javascript":"shBrushCpp.js",
        "Php":"shBrushJScript.js",
        "Python":"shBrushPython.js",
        "Ruby":"shBrushRuby.js",
        "Sql":"shBrushSql.js",
        "Vb":"shBrushVb.js",
        "Xml":"shBrushXml.js",
}
 
@csrf_protect
def new(request):
	form_codes = codesForm(initial={'date': datetime.date.today()})
	return render_to_response("new.html", {'form_code':form_codes},
                               context_instance=RequestContext(request))
@csrf_protect
def add(request):
	global language
	
	if request.method == "POST":
		form_codes = codesForm(request.POST)
		if form_codes.is_valid():
			form_codes.save()
			return HttpResponseRedirect('/list/')
	else:
		form_codes = codesForm()
		
	return render_to_response("new.html", {'form_code':form_codes},
                               context_instance=RequestContext(request))
	
def list(request):
    codigos = codes.objects.all().order_by('-date','name')
    return render_to_response('list.html', {'codigos': codigos})

def code(request, request_id, request_name):
    global language
    
    try:
        codigo = codes.objects.get(id=request_id, name=request_name)
        return render_to_response('code.html', {"codigo":codigo, "language": lenguajes[codigo.language.name]})
    except:
        return render_to_response('list.html', {'codigos': codes.objects.all()})
    

