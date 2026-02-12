from django.http import HttpResponse

def visualizarHome(request):
    return HttpResponse('<h1>Visualisando a home</h1>')