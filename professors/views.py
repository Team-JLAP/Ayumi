from django.shortcuts import render
from .dummy import generateProfList

def home(request):
    return render(request, 'professors/home.html')

def course_ratings(request, prof_id, course_name):
    target = generateProfList(1)[0]
    context = {'prof': target}
    return render(request, 'professors/course_ratings.html', context=context)

def search_prof(request, prof_name):
    profs = generateProfList(5)
    context = {'search_term': prof_name, 'results': profs}
    return render(request, 'professors/search_prof.html', context=context)

def search_course(request, subject, course_id):
    return render(request, 'professors/search_course.html')

def prof_course(request, prof_id):
    return render(request, 'professors/prof_course.html')

def rating(request, prof_id, course_name):
    return render(request, 'professors/rating.html', context={'prof_id': prof_id})



def login(request):
    return render(request, 'professors/login.html')

def signup(request):
    return render(request, 'professors/signup.html')

def profile(request, user_id):
    return render(request, 'professors/profile.html')

def profile_setting(request, user_id):
    return render(request, 'professors/profile_setting.html')