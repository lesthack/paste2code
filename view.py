'''
Created on 19/07/2011

@author: lesthack
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from pub.models import *
 
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
 
def new(request):
    form_codes = codesForm()
    return render_to_response('new.html', {'form': form_codes})

def list(request):
    codigos = codes.objects.all()        
    return render_to_response('list.html', {'codigos': codigos})

def code(request, request_id, request_name):
    global language
    
    try:
        codigo = codes.objects.get(id=request_id, name=request_name)    
        return render_to_response('code.html', {"codigo":codigo, "language": lenguajes[codigo.language.name]})
    except:
        return render_to_response('list.html', {'codigos': codes.objects.all()})
    

