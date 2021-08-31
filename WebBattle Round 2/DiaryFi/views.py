from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import diary
# Create your views here.

def sign(request):
    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, "index.html")

    context={}
    return render(request, "index.html", context)

def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        diary_name = request.POST['diary_name']
        content = request.POST['content']
        photo = request.POST['photo']

        add = diary.objects.create_diary(diary_name=diary_name, content=content, photo=photo)
        add.save();
        print('user created')
        return redirect('/')
    else:
        return render(request, 'add_new.html')

def old(request):
    contents= diary.objects.all()
    return render(request, 'old_daily_entries.html', {'contents': contents})

def view(request):
    return render(request, 'out.html')