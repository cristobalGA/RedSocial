"""aplicacion3 URL Configuration

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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',login,{'template_name': 'login.html'},name='login'),
    url(r'^logout/$',logout_then_login,name='logout'),
    url(r'^signup/$',Signup.as_view(),name='signup_view'),
    url(r'^$',index_view.as_view(),name='Index_view'),
    url(r'^publicacion-general/$',publicaion_genera_view,name='publicacion_general_view'),
    url(r'^publicacion/$',publicacion_view.as_view(),name='publicacion_view'),
    url(r'^comentario/$',comentario_view.as_view(),name='comentario_view'),
    url(r'^publicacion-perfil/$',publicaion_perfil,name='publicacion_perfil'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

