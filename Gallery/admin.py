#from django import forms
from django.contrib import admin
from .models import Visitor, Post
from django.db import models


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    image = models.ImageField("Photo")
    id = models.AutoField("Іd" ,primary_key=True)

    def __unicode__(self):
        return self.title



@admin.register(Visitor)

class VisitorAdmin(admin.ModelAdmin):
    id = models.AutoField("Id", primary_key=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField("IP address", max_length=15)
    dataTime = models.DateTimeField("Время")

    def __unicode__(self):
        return self.title
# Register your models here.
