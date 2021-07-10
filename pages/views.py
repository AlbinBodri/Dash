from django.http import HttpResponse, request
from django.shortcuts import render
from django.http import JsonResponse
from .models import Device

def home_view(request):
    #Gets all Device objects in database stores it in queryset variable as an array. 
    #queryset is passed on devices_list which is returned in context to template.
    queryset = Device.objects.all()
    context = {
    "devices_list": queryset,
    }
    return render(request, "home.html", context)


def toggle_button_view(request):
    if request.POST.get('action') == 'toggle_button':
        logfile_object = open('log.txt', 'a')
        token = request.POST.get('csrfmiddlewaretoken')
        print (token)
        id = request.POST.get("id")
        print (id)
        action = (Device.objects.get(id=id).action)
        print (action)
        logfile_object.write(f"Action: {action} was completed")
        logfile_object.write("\n")
        logfile_object.close()
        
    return render(request, "home.html")