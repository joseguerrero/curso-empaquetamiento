from django.http import HttpResponse

def saludo(request):
    html = "<html><body>Hola esta es la version web del saludador</body></html>"
    return HttpResponse(html)
