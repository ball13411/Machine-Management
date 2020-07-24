from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['inputUsername']
        passwd=request.POST['inputPassword']
        user = auth.authenticate(username=username,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"username หรือ password ไม่ถูกต้อง")
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        username = request.POST['inputUsername']
        firstname = request.POST['inputFirstName']
        lastname = request.POST['inputLastName']
        email = request.POST['inputEmailAddress']
        password = request.POST['inputPassword']
        con_password = request.POST['inputConfirmPassword']
        if password==con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"มีผู้ใช้ชื่อ Username นี้แล้ว")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"มีผู้ใช้ Email นี้แล้ว")
            else:
                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=firstname,
                    last_name=lastname,
                )
                user.set_password(password)
                user.save()
                user = auth.authenticate(username=username,password=password)
                auth.login(request,user)
                return redirect("/")
        else:
            messages.info(request,"รหัสผ่านไม่ตรงกัน กรุณาตรวจสอบใหม่")
        print(messages)
    return render(request,'register.html')
