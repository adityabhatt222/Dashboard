from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Post
from .forms import PostForm

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'html/home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same")
        else:
            
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already exists")
            
            
            try:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect("login")
            except IntegrityError:
                return HttpResponse("Failed to create user")
        
    return render(request, 'html/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse('Username or Password is incorrect or does not exist')

    return render(request, 'html/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  
    else:
        form = PostForm()
    return render(request, 'html/upload_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'html/post_list.html', {'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
    return redirect('post_list')