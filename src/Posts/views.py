from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_create(request):#create new post
    return HttpResponse("<html>Create </html>")

def posts_list(request): #retrieve list of items
    context={
        "title":"list"
    }
    return render(request, "index.html",context)

def posts_detail(request):#retrieve single item
    return HttpResponse("<html>Details </html>")

def posts_update(request): #update db
    return HttpResponse("""<html>
    <form>
  First name:<br>
  <input type="text" name="firstname"><br>
  Last name:<br>
  <input type="text" name="lastname">
</form></html>""",)

def posts_delete(request):#delete db
    return HttpResponse("<html>Delete</html>")