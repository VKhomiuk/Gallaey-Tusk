from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic.base import View
import datetime
from .models import Post, Visitor

from Gallery.forms import LoaderForm




class Load(View):

    def post(self, request):
        form = LoaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "add_image.html", {"form": form})








class AddImage(View):
    def get(self, request):
        return render(request, "add_image.html", {"form": LoaderForm()})


class Gallery(View):
    def get(self, request):
        images = Post.objects.all()
        images = reversed(images)
        return render(request, "index.html", {"image_list": images})


class PhotoPreview(View):

    def get_visitor_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


    def get(self,request,pk):
        photopreview = PhotoPreview()
        post = Post.objects.get(id=pk)
        Visitor.objects.create(postId=post, dataTime=datetime.datetime.now(), ip=photopreview.get_visitor_ip(request))
        return render(request, "preview.html", {"photo": post})

