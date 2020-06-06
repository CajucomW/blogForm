from django.shortcuts import render

def homepage_form(request):
    context = {}
    return render(request, 'homepage_form.html', context)
