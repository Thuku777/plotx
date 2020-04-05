"""plotx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls import url


urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('catalog/', include('catalog.urls')),
    path('churches/', include('churches.urls')),
    path('blog/', include('blog.urls')),
    path('realtors/', include('realtors.urls')),  
 
    path('companys/', include ('companys.urls')),  
    path('contact/', include('contact.urls')),
    path('listings/', include('listings.urls')),
    path('towns/', include('towns.urls')),
    path('locations/', include('locations.urls')),
    path('profile/', user_views.profile, name='profile' ),
    
    
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    

