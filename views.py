from django.http import HttpResponse
import datetime

def login(request):  #ESTO ES UNA VISTA

    pagina="<html><head><title>Welcomee</title>  </head><body><div class='welcome'><center><h1><font size='13' color='black'>Welcome</font></h1></center></div><center><hr></center><center><a href='/logout'>Logout</a></center><div class='breaker'><br /><br /><br /><br /><br /><br /><br /></div><div class='footer'><footer style='position: fixed; left: 2; right: 2; width: 95%; bottom: 0;'><center>This webpage is only accessible behind a User Web Login System written in Python</center></footer></div></body></html>"
    
    return HttpResponse(pagina)

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    fech="""<html><body><h1> La fecha y hora es   %s </h1></body></html>""" % fecha_actual

    return HttpResponse(fech)
    
    variable=null
