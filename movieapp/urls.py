"""
URL configuration for movieapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from movies.views import *
from account.urls import *


#http://127.0.0.1:8000/movies
#http://127.0.0.1:8000/movies/3
#http://127.0.0.1:8000/movies/walking-dead

router = DefaultRouter()
router.register(r'books', CombinedModelViewSet, basename='books')
router.register(r'cocukkitabi', Model2ViewSet, basename='cocukkitabi')
router.register(r'education', Model3ViewSet, basename='education')
router.register(r'macera', Model4ViewSet, basename='macera')
router.register(r'gerilim', Model5ViewSet, basename='gerilim')
router.register(r'biyografik', Model6ViewSet, basename='biyografik')
router.register(r'aksiyon', Model7ViewSet, basename='aksiyon')



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/allofthem', CombinedModelView.as_view(), name='combined-model'),
    #path("users/", views.UserModelView.as_view()),
    #path('add_user_view/', add_user_view, name='add_user_view'),
    path('api/', include(router.urls)),
    #path("users1/", views.UserModelView1.as_view()),
    #path('',include("apis.urls"))
    path('', include('account.urls')),
    path('comment/', include('movies.urls')),
    
]
