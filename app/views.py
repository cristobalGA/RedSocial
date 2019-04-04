# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
# Create your views here.
class index_view(TemplateView):
    template_name = 'index.html'

class Signup(FormView):
    template_name = 'signup.html'
    form_class = usuario_form
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = usuario()
        p.usuario = user
        p.nombre = form.cleaned_data['nombre']
        p.apellidos = form.cleaned_data['apellidos']
        p.edad = form.cleaned_data['edad']
        p.sexo = form.cleaned_data['sexo']
        p.email = form.cleaned_data['email']
        p.save()
        return super (Signup, self).form_valid(form)


def publicaion_perfil(request):
        comentarios = list(publicacion.objects.all())
        respuestas = list(comentario.objects.all())
        return render(request, 'muro.html',{'comentarios': comentarios, 'respuestas': respuestas})

    


def publicaion_genera_view(request):
    	comentarios = list(publicacion.objects.all())
        respuestas = list(comentario.objects.all())
    	return render(request, 'publicacion_general.html',{'comentarios': comentarios, 'respuestas': respuestas})


class publicacion_view(CreateView):
    template_name = 'publicacion_view.html',
    model = publicacion
    fields = '__all__'
    success_url = reverse_lazy('publicacion_view')

def comentarios(request):
    data = serializers.serialize('json', Usuarios.objects.all())
    return HttpResponse(data, content_type='aplication/json')

class comentario_view(CreateView):
    template_name = 'comentario.html'
    model = comentario
    fields = '__all__'
    success_url = reverse_lazy('comentario_view')