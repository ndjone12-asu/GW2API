from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def members(request):
    if request.method == "GET":
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
    elif request.method == "POST":
        template = loader.get_template('index.html')
        print(request.body.decode())
        return HttpResponse(template.render())
