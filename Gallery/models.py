from django.db import models

class Post(models.Model):
    image = models.ImageField("Photo", upload_to="media")
    id = models.AutoField("Id", primary_key=True)



class Visitor(models.Model):
    id = models.AutoField("Id", primary_key=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField("IP address", max_length=15)
    dataTime = models.DateTimeField("Время")

