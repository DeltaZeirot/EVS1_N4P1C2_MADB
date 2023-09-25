from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1r2(request):
    html= """
    
    <h1 style="color: orange">Pagina bienvenida a la rama 1</h1>
    
    """
    return HttpResponse(html)

def vista2r2(request):
    html="""
    
    <h1 style="font-family:Monocraft">Segunda vista de la rama 2</h1>
    
    <p style="font-family:Monocraft;color:orange">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt quia doloribus, quaerat natus ipsa itaque. Praesentium sequi, eius explicabo illo tempora distinctio repudiandae soluta? Nihil quae odit provident molestias assumenda.</p>
    
    """
    return HttpResponse(html)