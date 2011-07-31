'''
Created on 19/07/2011

@author: lesthack
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pub.models import *
from time import strftime
 
lenguajes = {
        "C":"shBrushCpp.js",
        "C++":"shBrushCpp.js",
        "C#":"shBrushCSharp.js",
        "Css":"shBrushCss.js",
        "Delphi":"shBrushDelphi.js",
        "Java":"shBrushJava.js",
        "Javascript":"shBrushJScript.js",
        "Php":"shBrushPhp.js",
        "Python":"shBrushPython.js",
        "Ruby":"shBrushRuby.js",
        "Sql":"shBrushSql.js",
        "Vb":"shBrushVb.js",
        "Xml":"shBrushXml.js",
}
 
@csrf_protect
def new(request):
	form_codes = codesForm(initial={'date':strftime("%Y-%m-%d %H:%M:%S")})
	return render_to_response("new.html", {'form_code':form_codes},
                               context_instance=RequestContext(request))
@csrf_protect
def add(request):
	global language
	
	if request.method == "POST":
		form_codes = codesForm(request.POST)
				
		if form_codes.is_valid():
			code = form_codes.save()
			return HttpResponseRedirect('/code/%d/' % code.id)
	else:
		form_codes = codesForm()
		
	return render_to_response("new.html", {'form_code':form_codes},
                               context_instance=RequestContext(request))
	
def list(request):
	codigos = codes.objects.all().order_by('-date','name')
	paginator = Paginator(codigos, 100)
	
	page = request.GET.get('page')
	
	if page == None:
		codigos = paginator.page(1)
	else:
		codigos = paginator.page(page)
	
	last_pages = paginator.num_pages
		
	return render_to_response('list.html', {'codigos':codigos, 'last_pages':last_pages})

def code(request, request_id):
    global language
    
    try:
        codigo = codes.objects.get(id=request_id)
        return render_to_response('code.html', {"codigo":codigo, "language": lenguajes[codigo.language.name]})
    except:
        return render_to_response('list.html', {'codigos': codes.objects.all()})
    
def about(request):
	return render_to_response('about.html', {})
