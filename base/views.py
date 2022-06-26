from django.shortcuts import render, get_object_or_404, redirect
from .forms import registerform, messageform
from .models import message
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = registerform()
    return render(request, "base/register.html", {"form":form})
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
            "massage": "invalid credentials"
            })
    return render(request, ("base/login.html"))
    

def logout_view(request):
    logout(request)
    return render(request, "base/login.html", {
    "message":"Logged out"
    })


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    users = User.objects.exclude(username=request.user.username)
    return render(request, ('base/home.html'), {
    'users': users
    })
# Create your views here.
def messages(request, sender, receiver):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    users = User.objects.exclude(username=request.user.username)
    person = request.user
    guy = User.objects.get(id=receiver)
    form = messageform()
    if request.method == 'POST':
        form = messageform(request.POST)
        if form.is_valid():
            chatmsg = form.save(commit=False)
            chatmsg.send = person
            chatmsg.receive = guy
            chatmsg.save()
            
    else:
        pass
    mess = message.objects.filter(send_id=person, receive_id=guy).order_by('id') | message.objects.filter(send_id=guy, receive_id=person).order_by('id')
    return render(request, ('base/messages.html'), {
        'form': form,
        'mess': mess,
        'guy': guy
        })