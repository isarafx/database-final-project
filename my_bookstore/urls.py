"""bookg3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.urls import path,include
from book_management import views


urlpatterns = [
    url('dbtable',views.dbtable),
    path('admin/', admin.site.urls),
    url('insert_book/', views.insert_book),
    url('insert_author/', views.insert_author),
    url('insert_publisher/', views.insert_publisher),
    url('update_book/', views.update_book),
    url('update_author/', views.update_author),
    url('update_publisher/', views.update_publisher),
    url('delete_book/', views.delete_book),
    url('delete_author/', views.delete_author),
    url('delete_publisher/', views.delete_publisher),
    url('accounts/profile/', views.home),
    url('home/', views.home),

    
    path('',include('book_management.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    
    
]


