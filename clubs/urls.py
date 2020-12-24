
from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('clubs/', views.all_clubs, name='clubs'),
    path('announcements/', views.announcement, name='announcement'),
    path('posts/', views.post, name='post'),
    path('message/', views.messages, name='message'),
    path('clubDetail/', views.clupDetail, name='clubDetail'),

]