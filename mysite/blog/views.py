from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.http import Http404 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from django.views.generic import ListView
# Create your views here.
class PostListView(ListView): 
    """ Alternative post list view """
    queryset = Post.published.all() 
    context_object_name = 'posts'
    aginate_by = 3 
    template_name = 'blog/post/list.html'
    
    
def post_list(request): 
    post_list = Post.published.all() # Pagination
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1) 
    
    try: 
        posts = paginator.page(page_number) 
    except PageNotAnInteger:
        # If page_number is not an integer get the first page 
        posts = paginator.page(1)
    except EmptyPage: # If page_number is out of range get last page of results 
        posts = paginator.page(paginator.num_pages)
        
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post/list.html', context )


def post_detail(request, year, month, day, post): 
    post = get_object_or_404( Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    context = {
        'post': post,
    }
    return render( request, 'blog/post/detail.html', context )