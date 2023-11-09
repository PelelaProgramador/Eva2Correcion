from django.shortcuts import render
from django.http import HttpResponse
from AppEmpresa.models import producto
import datetime

# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str (dt)
    return HttpResponse(s)

def renderTemplate(request):
    # Lógica para renderizar tu plantilla y devolver una respuesta
    data = {"nombre": "Dwaynne Johnsson", "id": 1, "email": "LaRoca@hotmail.com"}
    return render(request, 'template.html', data)

def productoData(request):
    productos = producto.objects.all()
    data = {'productos' : productos}
    return render(request, 'productos.html', data)