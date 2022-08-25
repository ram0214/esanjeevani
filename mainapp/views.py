from django.shortcuts import redirect, render, HttpResponse
from mainapp.models import UserInfo
from mainapp.forms import UserForm
from django.contrib import messages
from mainapp.models import UserInfo
# Create your views here.


def body_picker(request):
    return render(request, "mainapp/human-anatomy.html")

def organ(request):
    return render(request, "mainapp/internal_organs.html")
    
def chatbot(request):
    context = {
        'organ': None,

    }
    if request.GET.get('organ'):
        request.session['organ'] = request.GET.get('organ')
        context['organ'] = request.session.get('organ')
    return render(request, "mainapp/chatbot.html",context)


    

def doctor_page(request):
    user_info=UserInfo.objects.all()
    return render(request, "mainapp/doctor.html", {"user_info":user_info})


def home(request):
    if request.method=='POST':
        fullname=request.POST['name']
        email=request.POST['email']
        contact_no=request.POST['number']
        age=request.POST['age']
        problem=request.POST['problem']
        user=UserInfo.objects.create(fullname=fullname,email=email,contact_no=contact_no, age=age, problem=problem)
        user.save()
        messages.success(request,'Data has been submitted')
        return redirect("/")

    return render(request, "mainapp/home.html")    


def general_problem(request):
    general_problem=request.GET.get('general_problem','')
    return render(request, "mainapp/general_problem.html")   

   