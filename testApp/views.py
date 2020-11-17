from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    if request.method=='GET':
        form=forms.Login()
        return render(request,'testApp/home.html',{'form':form})
    if request.method=='POST':
        form=forms.Login(request.POST)
        if form.is_valid():
            name=request.POST['name']
            request.session['name']=name
            print('validations')
            print('email:',form.cleaned_data['email'])
            return amazon(request)
    return render(request,'testApp/home.html',{'form':form})

def amazon(request):
    return render(request,'testApp/amazon.html')

def history(request):
    return render(request,'testApp/history.html')

def about(request):
    return render(request,'testApp/about.html')

def feedback(request):
    form=forms.feedback()
    if request.method=='POST':
        form=forms.feedback(request.POST)
        if form.is_valid():
            print('feedback submitted succesfully')
            return amazon(request)
    return render(request,'testApp/feedback.html',context={'form':form})

def products(request):
    return render(request,'testApp/products.html')

def second(request):
    return render(request,'testApp/second.html')

def third(request):
    return render(request,'testApp/third.html')

def fourth(request):
    return render(request,'testApp/fourth.html')

def buyt(request):
    return render(request,'testApp/tshirt.html')

def logout(request):
    form=forms.logout()
    return render(request,'testApp/logout.html',{'form':form})

def mobile(request):
    return render(request,'testApp/mobile.html')

def laptop(request):
    return render(request,'testApp/laptop.html')

def vehicle(request):
    return render(request,'testApp/vehicle.html')

def clothes(request):
    return render(request,'testApp/clothes.html')

def earphone(request):
    return render(request,'testApp/earphone.html')

def shoes(request):
    return render(request,'testApp/shoes.html')

def football(request):
    return render(request,'testApp/football.html')

def volleyball(request):
    return render(request,'testApp/volleyball.html')

def cricket(request):
    return render(request,'testApp/cricket.html')

def tennis(request):
    return render(request,'testApp/tennis.html')

def toys(request):
    return render(request,'testApp/toys.html')

def shirts(request):
    return render(request,'testApp/shirts.html')
