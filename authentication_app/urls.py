from django.urls import include, path
from . import views

urlpatterns = [
    #authentication related link
    path('', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),

]
