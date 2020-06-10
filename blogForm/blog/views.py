from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from .models import BlogPost
from .forms import PostForm

class PostBlog(forms.Form):
    print("---Used PostBlog---")
    username = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

# class BlogPost(ListView):
#     print('---BlogPost Loaded---')
#     model = BlogPost
#     template_name = "homepage_form.html"

# class AddPost(CreateView):
#     print('---AddPost Loaded---')
#     model = BlogPost
#     form_class = PostForm
#     template_name = "homepage_form.html"

def homepage_form(request):
    print("---Viewed Homepage---")
    posts = BlogPost.objects.order_by('-created')
    if request.method == 'POST':
        form = PostBlog(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            text = form.cleaned_data['text']
            BlogPost.objects.create(
                username=username,
                text=text,
            )
            return redirect('/')
    else:
        form = PostBlog() 
        
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'homepage_form.html', context)