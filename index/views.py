from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def company(request):
    return render(request,'company.html')
def meet_the_team(request):
    return render(request,'meet_the_team.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def work(request):
    return render(request,'work.html')

def contact(request):
    return render(request,'contact.html')

