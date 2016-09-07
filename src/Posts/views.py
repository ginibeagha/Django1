from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_create(request):#create new post
    return HttpResponse("<html>Create </html>")

def posts_list(request): #retrieve list of items
    return HttpResponse("<html>List</html>")

def posts_detail(request):#retrieve single item
    return HttpResponse("<html>Details </html>")

def posts_update(request): #update db
    return HttpResponse("<html>Update</html>")

def posts_delete(request):#delete db
    return HttpResponse("<html>Delete</html>")