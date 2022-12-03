from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'professors/home.html')

def prof(request, prof_id):

    return render(request, 'professors/prof.html', context={'prof_id': prof_id})

def search_result(request, prof_name):
    return render(request, 'professors/search_result.html', context={'search_term': prof_name})

def login(request):
    return render(request, 'professors/login.html')

def rating(request, prof_id):
    return render(request, 'professors/rating.html', context={'prof_id': prof_id})