from django.shortcuts import render

# Create your views here.
def perfil_pessoa(request):
    return render(request, 'curriculo/carta.html', {})