from django.urls import path 
from . import views

urlpatterns = [
    path('', views.mi_vista, name="index"),
    path('download/', views.download, name="download"),
]
