from events.models import Event
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import Http404
from .models import Post, Tag, Category, Comment

# Create your views here.
def index(request):
    context = {
        'news': Post.objects.order_by('-date_created').all(),
        'categories': Category.objects.order_by('name').all(),
        'sidebar_events': [i for i in Event.objects.order_by('-created_on').all()][:5]
    }
    return render(request, 'blog/index.html', context)


def single(request, slug):
    # try:
    #     post = Post.objects.filter(slug=slug)
    # except Exception as err:
    #     raise Http404('Post does not exist')

    # loop over posts in chronological order
    # posts = list(Post.objects.order_by('date_created'))
    # for idx, p in enumerate(posts):
    #     if post == p:
    #         try:
    #             next_post = posts[idx+1]
    #             has_next = True
    #         except IndexError as err:
    #             next_post = None
    #             has_next = False
    #         if idx-1 == -1:
    #             prev_post = None
    #             has_prev = False
    #         else:
    #             prev_post = posts[idx-1]
    #             has_prev = True
    n = get_object_or_404(Post, slug=slug)
    context = {
        'n': n.to_dict(),
        'news': [i for i in Post.objects.order_by('-date_created').all() if i != n]
        # 'post': post.to_dict(),
        # 'tags': [t for t in Tag.objects.all() if t.post.id == post.id],
        # 'recent_posts': [p.to_dict() for p in Post.objects.order_by('-date_created')][:10],
        # 'all_tags': list(set([i.name.lower() for i in Tag.objects.all()]))[:50],
        # 'categories': Category.objects.all()[:10],
        # 'comments': [c.to_dict() for c in Comment.objects.filter(post=post)],
        # 'has_next': has_next,
        # 'next_post': next_post,
        # 'has_prev': has_prev,
        # 'prev_post': prev_post
    }
    return render(request, 'blog/single.html', context)

def comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        form = request.POST
        c = Comment(name=request.POST.get('name'), email=request.POST.get('email'), site=request.POST.get('site') if request.POST.get('site') else '', text=request.POST.get('message'), post=post)
        c.save()
        return redirect('blog.single', post_id=post_id)

def tags(request, tag_slug):
    context = {
        'posts': [t.post for t in Tag.objects.filter(slug=tag_slug)],
        'categories': Category.objects.order_by('name'),
    }
    return render(request, 'pages/blog/index.html', context)