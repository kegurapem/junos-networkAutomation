from django.urls import path 
from . import views

urlpatterns = [
    
    path('home/', views.HomePage, name="home"),
    path('signup/', views.SignupPage, name="signup"),
    path('', views.LoginPage, name="login"),
    path('logout/', views.LogoutPage, name="logout"),
    path('download/', views.descargar_json, name="download"),
    # path('history/', views.history, name="history"),
    path('usersnornir/', views.usuarios_nornir, name="usersnornir"),
    path('listusersnornir/', views.list_usuarios_norrnir, name="listusersnornir"),

    # A partir de aquí corren los urls funcnionales
    path('home1/', views.HomePage, name="home1"),
    path('signup1/', views.SignupPage, name="signup1"),
    path('login1/', views.LoginPage, name="login1"),
    path('logout1/', views.LogoutPage, name="logout1"),
    path('usersnornir2/', views.users_nornir, name="usersnornir2"),
    path('listusersnornir2/', views.list_users_nornir, name="listusersnornir2"),
    path('config/', views.config, name="config"),
    path('configuration', views.mi_vista, name="configuration"),
    # path('downloadbackup', views.downloadbackup, name="downloadbackup"),
    path('download_backup/', views.download_backup, name='downloadbackup'),
     path('factorydefault', views.factoryDefault, name='factory'),
]
