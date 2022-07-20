from django.shortcuts import render, get_object_or_404
from .models import post
# Create your views here.
def render_post(request ):
    blog = post.objects.all()
    return render (request, 'posts.html', {'blog':blog})

def detail_post(request, post_id):
    # detalle = post.objects.get(id=post_id)
    posts = get_object_or_404(post, pk=post_id)
    return render(request, 'post_detail.html',{ 'posts': posts})