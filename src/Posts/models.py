from django.db import models

# Create your models here.
class Post(models.Model):
    Title= models.CharField(max_length=120)
    content=models.TextField(blank=True)
    picture= models.FileField(upload_to='./')
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedTime=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.Title