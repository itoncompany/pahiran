from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request,'Authentications/login.html')

def create_account(request):
    return render(request,'Authentications/create-account.html')
def dashboard(request):
    return render(request,'Authentications/user-profile.html')