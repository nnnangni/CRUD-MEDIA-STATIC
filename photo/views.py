from django.shortcuts import render, redirect
from .models import Photo, Comment

# Create your views here.
def list(request):
    photos = Photo.objects.all()
    return render(request, "photo/list.html",{"photos":photos})

def create(request):
    if request.method == "POST":
        # POST방식으로 들어왔을 때
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        Photo.objects.create(title=title, content=content, image=image)
        
        return redirect("photos:list")
    else:
        # GET방식으로 들어왔을 때
        return render(request,"photo/create.html")
        
def detail(request, id):
    photo = Photo.objects.get(id=id)
    comment = Comment.objects.filter()
    return render(request,"photo/detail.html",{"photo":photo})
    
def update(request, id):
    photo = Photo.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        photo.title = title
        photo.content = content
        photo.save()
        
        return redirect("photos:detail",id)
    else:
        # GET방식으로 들어왔을 때
        
        return render(request,"photo/update.html", {"photo":photo})
        
def delete(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect("photos:list")
    
def comment_create(request, id):
    photo = Photo.objects.get(id=id)
    content = request.POST.get("content")
    Comment.objects.create(photo=photo, content=content)
    
    return redirect("photos:detail", id)
    