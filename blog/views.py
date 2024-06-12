from django.shortcuts import render,redirect
from .models import Tags,Category,Blog,Comments
from .forms import CommentsForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# blog view
def blog_view(request):
    blog=Blog.objects.all()
    context={"blog":blog}
    return render(request,"blog/blog_view.html",context)

# detail of blog and category and tags and comment view
def detail_view(request,id=None):
    category=Category.objects.all()
    tags=Tags.objects.all()
    blog=Blog.objects.get(id=id)
    
    comment=Comments.objects.filter(blog=blog)
    if request.method=="POST":
        form=CommentsForm(request.POST)
        if form.is_valid():
            blog1=Blog.objects.get(id=id)
            # name=User.objects.get(username=request.user.username)
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            newcomment=Comments(name=name,email=email,message=message,blog=blog1)
            newcomment.save()
            return redirect("blog:detail_view",id)
        # else:
        #     return HttpResponse("invalid input")
    else:
        form=CommentsForm
        context={"category":category,"tags":tags,"form":form,"blog":blog,"comment":comment}
        return render(request,"blog/detail_view.html",context)    
        
    






    
    

    
# blog=Blog.objects.all().filter(category=category1,tag=tags)
        
# return render(request,"blog/detail_view.html",context)
    
    
# def detail_view(request,id=None):
    
    
#     category=Category.objects.all()
#     tags=Tags.objects.all()
    
    
#     if id:
#         category1=Category.objects.get(id=id)
#         tag1=Tags.objects.get(id=id)
#         blog=Blog.objects.all().filter(category=category1,tag=tag1)
    
#         # blog=Blog.objects.all().filter(category=category1,tag=tags)
        
#     if request.method=="POST":
#         form=CommentsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("blog:detail_view")
#         else:
#             return HttpResponse("invalid input")
#     else:
#         form=CommentsForm
#         context={"category":category,"tags":tags,"form":form,"blog":blog}
#         return render(request,"blog/detail_view.html",context)
#     # return render(request,"blog/detail_view.html",context)
    