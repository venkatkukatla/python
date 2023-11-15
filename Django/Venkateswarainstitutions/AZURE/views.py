from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def azure(request):
    values={"name":"azure","duration":"days60","cloud":"Azure cloud"}
    return render(request,'AZURE/azure.html',values)

def ado(request):
    return render(request,'AZURE/ado.html')
