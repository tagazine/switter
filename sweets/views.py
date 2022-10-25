import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Sweets
from .forms import SweetForms

def home(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def sweet_create_view(request, *args, **kwargs):
    form = SweetForms(request.POST or None)
    if form.is_valid:
        obj = form.save(commit=False)
        obj.save()
        form = SweetForms
    return render(request, "components/form.html", context={"form": form})

def sweet_list(request, *args, **kwargs):
    qs = Sweets.objects.all()
    s_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,1000)} for x in qs]
    data = {
        "isUser": False,
        "response": s_list
    }
    return JsonResponse(data)

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


