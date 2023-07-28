from django.shortcuts import render

# Create your views here.
def userdeffilter(request):
    d={'data':'Hai Jarvis'}
    return render(request,'userdeffilter.html',d)

