"""pro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app2.views import model_form_upload
from .views import login_page,home_page, logout_page,contact_page,dept
from django.conf import settings
from django.conf.urls.static import static
from subjects.views import Books, Articles, Papers, cse_watch,ece_watch,it_watch, read

urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^upload/$',model_form_upload,name='upload'),
    url(r'^login/$',login_page,name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^logout/$',logout_page,name="logout"),
    url(r'^books/$',Books,name="books"),
    url(r'^articles/$',Articles,name="articles"),
    url(r'^papers/$',Papers,name="papers"),
    url(r'^cse_watch/$',cse_watch,name="cse_watch"),
    url(r'^ece_watch/$',ece_watch,name="ece_watch"),
    url(r'^it_watch/$',it_watch,name="it_watch"),
    url(r'^read/$',read,name="read"),
    url(r'^dept/$',dept,name="dept"),
    url(r'^contact/$',contact_page,name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
