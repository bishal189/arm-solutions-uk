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
    if request.method=="GET":
        return render(request,'contact.html')
    if request.method=="POST":
        try:
            print(request.body)
        except Exception as e:
            print(e)
            return render(request,'contact.html',{"error":str(e)})
def services(request):
    return render(request,'services.html')
