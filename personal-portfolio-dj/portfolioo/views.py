from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']


        send_mail(name , message , settings.EMAIL_HOST_USER , [email] , fail_silently=False)
        return render(request , 'index.html' , {'email': email , 'number': number})

        
    context = {
        'posts': posts
    }
    return render(request , 'index.html' , context)