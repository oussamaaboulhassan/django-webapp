from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name= "Hello World!" ),
    path("proexp/", views.exp, name="Experiences"),
    path("projects/", views.proj, name="Projects"),
    path("skills/", views.skills, name="Skills"),
    path("contact/", views.contact, name="Contact me!"),
    path("degrees/",views.degree, name= "Degrees"),
]
