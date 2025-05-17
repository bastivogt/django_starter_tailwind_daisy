from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
import os

# Create your views here.


def page(request, name):
    file_name = f"{name}.html"
    file_path = os.path.join(settings.BASE_DIR, "pages", "templates", "pages", file_name)
    if not os.path.isfile(file_path):
        raise Http404()
    
    return render(request, f"pages/{file_name}", {
        "title": name.title()
    })
        


def index(request):
    return render(request, "pages/index.html", {
        "title": "pages#index"
    })
