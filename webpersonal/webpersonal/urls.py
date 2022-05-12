"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from core import views as core_view
from portfolio import views as portfolio_view

from django.conf import settings

urlpatterns = [
    path('', core_view.home, name='home'),
    path('about', core_view.about, name='about'),
    path('portfolio', portfolio_view.portfolio, name='portfolio'),
    path('contact', core_view.contact, name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)