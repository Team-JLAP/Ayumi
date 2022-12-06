from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prof=<int:prof_id>/<str:course_name>/', views.course_ratings, name='course_ratings'),
    path('search/prof=<str:prof_name>/', views.search_prof, name='search_prof'),
    path('search/subject=<str:subject>/id=<int:course_id>/', views.search_course, name='search_course'),
    path('course/prof=<str:prof_name>/', views.prof_course, name='prof_course'),
    path('login/', views.login, name='login'),
    path('rating/prof=<int:prof_id>/<str:course_name>/', views.rating, name='rating')
    # user profile, profile setting, etc.
]
