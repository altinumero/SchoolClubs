

from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('clubs/', views.all_clubs, name='clubs'),


    path('announcements/', views.announcement, name='announcement'),
    path('posts/', views.post, name='post'),
    path('chat/', views.chat, name='chat'),
    path('surveys/', views.survey, name='survey'),
    path('discussions/', views.discussion, name='discussion'),


    path('message/', views.messages, name='message'),
    path('clubDetail/', views.clupDetail, name='clubDetail'),

    path('addpost/', views.addPost, name='addPost'),
    path('addevent/', views.addEvent, name='addEvent'),
    path('addsurvey/', views.addSurvey, name='addSurvey'),
    path('adddiscussion/', views.addDiscussion, name='addDiscussion'),
    path('join/', views.join, name='join'),
    path('report/', views.report, name='report'),

    path('userpage/', views.userPage, name='userpage'),

]
