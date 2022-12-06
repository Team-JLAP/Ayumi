from django.shortcuts import render
from .dummy import generateProfList

def home(request):
    return render(request, 'professors/home.html')

def prof(request, prof_id):
    target = generateProfList(1)[0]
    context = {'prof': target}
    return render(request, 'professors/prof.html', context=context)

def search_result(request, prof_name):
    profs = generateProfList(5)
    context = {'search_term': prof_name, 'results': profs}
    return render(request, 'professors/search_result.html', context=context)

def login(request):
    return render(request, 'professors/login.html')

def rating(request, prof_id):
    return render(request, 'professors/rating.html', context={'prof_id': prof_id})