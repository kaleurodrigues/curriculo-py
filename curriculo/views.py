from django.shortcuts import render
from .models import DadosPessoa

# Create your views here.
def perfil_pessoa(request):
    var = DadosPessoa.objects.get(name="Kaleu Silva Rodrigues")
    return render(request, 'curriculo/carta.html', {"var": var})
