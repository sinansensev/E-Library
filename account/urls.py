from django.urls import path
from . import views
from account import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]
