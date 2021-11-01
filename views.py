from django.http import HttpResponse
import datetime
import pyotp
import qrcode
from django.template import Template, Context

def login(request):  #ESTO ES UNA VISTA
   
    
 #codigo de nico (funciona)
    clave = pyotp.random_base32()
    #print("Clave:", clave)
    totp_object = pyotp.TOTP(clave)
    #Se realiza la Autenticacion por medio de otp utilizando el algoritmo de totp
    qr_text = totp_object.provisioning_uri(name="2FA", issuer_name="Seguridad")
    #print(qr_text)
    #Genera un QR
    img = qrcode.make(qr_text)
    f = open("output.png", "wb")
    img.save(f)
    f.close()

    #Validar con el Google Authenticator ingresando el codigo que te genera
    otp = input("ingresar el OTP: ")
    validar = totp_object.verify(otp)
    #print(validar)
    



    #Cargar la direccion de la plantilla de html en la variable plantilla_externa
    plantilla_externa=open("C:/Users/Silencer/Documents/UNIVERSIDAD/4TO AÑO/SEGUNDO SEMESTRE/Arq Palma/python/pythonFrontEnd/Plantillas/PlantillaLogin.html")
    plt=Template(plantilla_externa.read())
    nombre="Juan"
    plantilla_externa.close() #se cierra luego de consumierlo para ahorrar recursos

    ctx=Context({"nombre_persona":nombre}) #context puede recibir diccionarios como parametros, un diccionario tiene una clave y un valor
    #la variable pagina consume el documento abierto en plt para renderizarlo con el metodo render y el contexto como argumento de render 
    pagina=plt.render(ctx)

    return HttpResponse(pagina)







def damefecha(request):

    fecha_actual=datetime.datetime.now()

    fech="""<html><body><h1> La fecha y hora es ñ  %s </h1></body></html>""" % fecha_actual

    return HttpResponse(fech)

  
