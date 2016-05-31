from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import render, Http404
from django.db import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Post, Comment, Points_Post, Points_Comment


def detail(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        p.post_views = getattr(p, 'post_views') +1;
        p.save()

    except p.DoesNotExist:
        return render(request, 'post/DoesNotExist.html')
    return render(request, 'post/detail.html', {'post': p, 'comment': out})


def user_post_like(request):

    return None


def user_post_dislike(request):
    current_user = request.user
    current_post = request.post
    user_post_like = Points_Comment.objects.filter(Post=current_post, User=current_user)

    if user_post_like is None:
        like = Points_Post
        like.points_comment_user = current_user
        like.points_comment_post = current_post
        like.points_comment_vote = 'D'
        like.save()

        current_post.post_points = getattr(current_post.post_points, 'post_views') -1;
        current_post.post_points.save()

    return None


def user_post_favorite(request):
    current_user = request.user
    current_post = request.post
    user_post_like = Points_Comment.objects.filter(Post=current_post, User=current_user)

    if user_post_like is None:
        like = Points_Post
        like.points_post_user = current_user
        like.points_post_post = current_post
        like.points_post_isFavorited= 'Y'
        like.save()

    return None


def post_comment(request):

    if request.POST:
        comment = request.POST.get('comment_text', '')
        current_user = request.user
        post_id = request.POST.get('pk', '')
        p = Post.objects.get(pk=post_id)

        if comment is not "" :
            tmp = Comment(comment_text=comment, comment_user=current_user, comment_post=p)
            tmp.save()
            out = Comment.objects.filter(comment_post=post_id)
            return render(request, 'post/detail.html', {'post': p, 'comment': out})












