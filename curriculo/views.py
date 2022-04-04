from django.shortcuts import render
from .models import DadosPessoa

# Create your views here.
def perfil_pessoa(request):
    var = DadosPessoa.objects.values()
    return render(request, 'curriculo/carta.html', {"var": var})