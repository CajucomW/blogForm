from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.homepage_form, name='homepage'),
]
