from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('api/get-quiz/', views.get_quiz, name = "get_quiz"),
    path('', views.home, name = "home"),
    path('quiz/', views.quiz, name = "quiz")
]
