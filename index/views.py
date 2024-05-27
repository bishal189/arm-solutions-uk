from django.shortcuts import render
from index.models import Contact
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
            data=request.POST
            full_name=data.get('full_name',"")
            email=data.get('email',"")
            phone_number=data.get("phone_number")
            help=data.get("help","")
            company=data.get('company','')
            Contact.objects.create(full_name=full_name,email=email,phone_number=phone_number,help=help,company=company)
            referer = request.POST.get('referer', '/')
            print(referer)
            return redirect(referer)
        except Exception as e:
            print(e)
            return render(request,'contact.html',{"error":str(e)})

def services(request):
    return render(request,'services.html')
