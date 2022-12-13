from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profid=<int:prof_id>/<str:course_name>/', views.course_ratings, name='course_ratings'),
    path('search/prof=<str:prof_name>/', views.search_prof, name='search_prof'),
    path('search/subject=<str:subject>/id=<str:course_id>/', views.search_course, name='search_course'),
    path('course/profid=<int:prof_id>/', views.prof_course, name='prof_course'),
    path('rating/profid=<int:prof_id>/course=<str:course_name>/', views.rating, name='rating'),
    
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/userid=<int:user_id>/', views.profile, name='profile'),
    path('profile/setting/userid=<int:user_id>/', views.profile_setting, name='profile_setting')
]
