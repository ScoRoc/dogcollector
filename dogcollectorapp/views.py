from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dog
from .forms import DogForm, LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    dogs = Dog.objects.all()
    form = DogForm()
    # render(request, template, context)
    return render(request, 'index.html', { 'dogs': dogs, 'form': form })

def show(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'show.html', { 'dog': dog })

def post_dog(request):
    form = DogForm(request.POST)
    if form.is_valid():
        dog = form.save(commit = False)
        dog.user = request.user
        dog.save()
    return HttpResponseRedirect('/')

def profile(request, user_name):
    user = User.objects.get(username=user_name)
    dogs = Dog.objects.filter(user=user)
    return render(request, 'profile.html', { 'username': user_name, 'dogs': dogs })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('This account has been disabled')
            else:
                print('The username and/or password is incorrect')
    else:
        form = LoginForm()
        return render(request, 'login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', { 'form': form })

def like_dog(request):
    dog_id = request.GET.get('dog_id', None)
    likes = 0
    if (dog_id):
        dog = Dog.objects.get(id=int(dog_id))
        if dog is not None:
            likes = dog.likes + 1
            dog.likes = likes
            dog.save()
    return HttpResponse(likes)







































    
