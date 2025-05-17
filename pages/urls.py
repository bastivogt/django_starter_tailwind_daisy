from django.urls import path
from .views import index, page

app_name = "pages"
urlpatterns = [
    path("<str:name>/", page, name="page"),
    path("", index, name="index")
]
