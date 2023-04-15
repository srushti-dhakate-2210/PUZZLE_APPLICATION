from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.Signup.as_view(),name="signup"),
    path('start',views.game,name="game"),
    path('authenticate/<int:no>/',views.auth,name='auth'),
    path('board',views.board,name="board"),

]
