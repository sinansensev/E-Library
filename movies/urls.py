from django.urls import path
from django.urls import path
from . import views
#http://127.0.0.1:8000/movies
#http://127.0.0.1:8000/movies/3
#http://127.0.0.1:8000/movies/walking-dead

urlpatterns = [
    path("",views.home),
    path("Home",views.home),
    #path("CareBook",views.movies),
    #path("Thriller",views.movies),
    #path("Action",views.movies),
    #path("ScienceFiction",views.movies),
    #path("Thriller",views.movies),
    #path("Biographic",views.movies),
    #path("Education",views.movies),
    
]