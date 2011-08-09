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
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
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
    form_codes = codesForm()
    
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
    paginator = Paginator(codigos, 30)
    
    page = request.GET.get('page')
    
    if page == None:
        codigos = paginator.page(1)
    else:
        codigos = paginator.page(page)
    
    last_pages = paginator.num_pages
        
    return render_to_response('list.html', {'codigos':codigos, 'last_pages':last_pages})

def fork(request, request_id):
    codigo = codes.objects.get(id=request_id)    
    form_codes = codesForm(initial={"code":codigo.code, 
                                    "language":codigo.language})
    
    return render_to_response("new.html", {'form_code':form_codes},
                               context_instance=RequestContext(request))
                               
def code(request, request_id):
    global language
    
    try:
        
        current_site = request.build_absolute_uri()
        codigo = codes.objects.get(id=request_id)
        lexer = get_lexer_by_name(codigo.language.name, stripall=True)
        formatter = HtmlFormatter()
        codigo.code = highlight(codigo.code, lexer, formatter)
        
        return render_to_response('code.html', {"codigo":codigo , "url":current_site})
    except:
        return render_to_response('list.html', {'codigos': codes.objects.all()})
    
def about(request):
    return render_to_response('about.html', {})
