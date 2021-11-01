from django.http import HttpResponse
import datetime
from django.template import Template, Context

def login(request):  #ESTO ES UNA VISTA
    #Cargar la direccion de la plantilla de html en la variable plantilla_externa
    plantilla_externa=open("C:/Users/Silencer/Documents/UNIVERSIDAD/4TO AÑO/SEGUNDO SEMESTRE/Arq Palma/python/pythonFrontEnd/Plantillas/PlantillaLogin.html")

    plt=Template(plantilla_externa.read())

    plantilla_externa.close() #se cierra luego de consumierlo para ahorrar recursos

    ctx=Context()
    #la variable pagina consume el documento abierto en plt para renderizarlo con el metodo render y el contexto que en este caso es vacio
    pagina=plt.render(ctx)

    return HttpResponse(pagina)

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    fech="""<html><body><h1> La fecha y hora es ñ  %s </h1></body></html>""" % fecha_actual

    return HttpResponse(fech)

    variable=null
