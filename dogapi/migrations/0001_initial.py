# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('size', models.CharField(max_length=20)),
                ('friendliness', models.IntegerField()),
                ('trainability', models.IntegerField()),
                ('sheddingamount', models.IntegerField()),
                ('exerciseneeds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('color', models.CharField(max_length=50)),
                ('favoritefood', models.CharField(max_length=50)),
                ('favoritetoy', models.CharField(max_length=50)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DogBreed', to='dogapi.Breed')),
            ],
        ),
    ]
