from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Post, Comment

def get_post_list(request):
    query = request.GET.get('search')

    if query:
        posts_list = Post.objects.annotate(
            comments_count=Count('comments') 
        ).filter(title__icontains=query).order_by('-created_at')
    else:
        posts_list = Post.objects.annotate(
            comments_count=Count('comments')
        ).all().order_by('-created_at')

    paginator = Paginator(posts_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj, 
        'query': query
    })

def get_post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:  
            Post.objects.create(title=title, content=content)
            return redirect('post_list') 
    
    return render(request, 'blog/post_form.html')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == "POST":
        text = request.POST.get('content')
        author = request.POST.get('author_name')
        
        if text:
            Comment.objects.create(
                post_id=post, 
                content=text, 
                author_name=author or 'Гість'
            )
            return redirect('post_detail', post_id=post.pk)
    
    return redirect('post_detail', post_id=post.pk)