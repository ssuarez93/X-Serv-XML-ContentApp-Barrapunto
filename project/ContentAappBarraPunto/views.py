# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from xml_parser_barrapunto import parse
from django.views.decorators.csrf import csrf_exempt
from models import Pages

# Create your views here.

@csrf_exempt
def identificador(request, ident):
    metodo = request.method
    titulares = parse()
    if metodo == "GET":
        try:
            pages = Pages.objects.get(id=int(ident))
            pagina = str(pages.page)
        except Pages.DoesNotExist:
            pagina = ("<h4>Error. No hay pagina para el identificador introducido</h4>")
    else:
        pagina = ("<h4>Error. Mediante un identificador solo se puede hacer GET de dicha pagina.</h4>")
    return HttpResponse(pagina + titulares)

@csrf_exempt
def recurso(request, recurso):
    metodo = request.method
    titulares = parse()
    if metodo == "GET":
        try:
            pages = Pages.objects.get(name=recurso)
            pagina = str(pages.page)
        except Pages.DoesNotExist:
            pagina = ("<h4>Error. No hay pagina para el recurso introducido.</h4>")
    elif metodo == "PUT":
        titulares = ""
        try:
            pages = Pages.objects.get(name=recurso)
            pagina = ("La pagina que usted quiere añadir ya está en la lista de paginas. Compruebe antes.")
        except Pages.DoesNotExist:
            cuerpo = request.body
            nueva = Pages(name=recurso, page=cuerpo)
            nueva.save()
            pagina = ("La pagina ha sido añadida.")
    else:
        pagina = ("Ha ocurrido algún error, solo se puede realizar GET o PUT.")
    return HttpResponse(pagina + titulares)

@csrf_exempt
def lista_paginas(request):
    try:
        inicio = ("<h3>Lista de paginas almacenadas: </h3>")
        lista_pages = Pages.objects.all()
        pagina = ""
        for page in lista_pages:
            pagina += "<li><a href='/" + str(page.id) + "'>" + str(page.name) + "</a>"
    except Pages.DoesNotExist:
        pagina = ("Ha ocurrido un error. No hay paginas almacenadas")
    return HttpResponse(inicio + pagina)

def update(request):
    titulares = parse()
    return HttpResponse("<h3>Los titulares se han actualizado</h3>")
