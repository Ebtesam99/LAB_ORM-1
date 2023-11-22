from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog


def addBlog(request : HttpRequest):

    if request.method == "POST":
        
        newBlog = Blog(title = request.POST["title"] , content = request.POST["content"] ,
                       is_published=  request.POST["is_published"] , published_at = request.POST["published_at"])
        newBlog.save()
        return redirect("blog:displayBlog")

    return render(request, "blog/addBlog.html")


def displayBlog(request : HttpRequest):
    blogs = Blog.objects.all()
    return render(request ,"blog/display.html" , {"blogs" : blogs})


def detailsBlog(request : HttpRequest ,blog_id):
    try: 
       blog = Blog.objects.get(id = blog_id)
    except  Exception as e:

       return render(request, "main/not_found.html")
       
    return render(request ,"blog/details.html" , {"blog" : blog})

