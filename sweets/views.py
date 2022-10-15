from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Sweets

def home(request, *args, **kwargs):
    return render(request, "pages/home.html", context={})

def sweet_details(request, sweet_id, *args, **kwargs):
    data = {
        "id": sweet_id,
        # "content": obj.content,
        # "image": obj.image.url
    }
    status = 200
    try:
        obj = Sweets.objects.get(id=sweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404
    
    

    return JsonResponse(data, status=status)


