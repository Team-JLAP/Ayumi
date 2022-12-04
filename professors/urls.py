from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prof/<int:prof_id>/', views.prof, name='prof'),
    path('search/<str:prof_name>/', views.search_result, name='search_result'),
    path('login/', views.login, name='login'),
    path('rating/<int:prof_id>/', views.rating, name='rating')
    # user profile, profile setting, etc.
]
