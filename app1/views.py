from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1r1(request):
    html= """
    
    <h1 style="color: red">Bienvenida rama1</h1>
    
    """
    return HttpResponse(html)

def vista2r1(request):
    html="""
    
    <h1 style="font-family:Monocraft">Segunda vista de la rama 1</h1>
    
    """
    return HttpResponse(html)