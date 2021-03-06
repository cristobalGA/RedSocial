# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 19:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('texto', models.TextField()),
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Edad', models.IntegerField(blank=True, null=True)),
                ('Sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.publicacion'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
