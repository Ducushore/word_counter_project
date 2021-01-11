"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views  # "." means "this folder"


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('emptyinput/', views.countpage, name='emptyinput'),

    path('count/', views.countpage, name='count'),  # name='count' is linked with "{% URL 'count' %}" from the 'home.html' template, and has nothing to do with 'count/' path name, or with 'views.count' name.
    # path('countthewords/', views.countpage, name='count'),  # So, the path name can be changed, even so the 'count.html' page will be rendered correctly, meaning that this line is doing the same as previous

]

