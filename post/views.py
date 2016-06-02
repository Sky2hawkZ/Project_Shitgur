from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import render, Http404, get_object_or_404
from django.db import models
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from models import Post, Comment, Points_Post, Points_Comment
from forms import UploadImageForm
from datetime import datetime
>>>>>>> origin/master

def index(request):
    all_gallery_posts = Post.objects.all()
    context = {'all_gallery_posts': all_gallery_posts}
    return render(request, 'post/frontpage.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=new_id)
        out = Comment.objects.filter(comment_post=new_id)
        post.post_views = getattr(post, 'post_views') + 1
        post.save()
        return render(request, 'post/detail.html', {'post': post, 'comment': out})
    except Post.DoesNotExist:
        raise Http404()

def upload_post(request):
    upload_form = UploadImageForm(request.POST or None, request.FILES)
    context = {'upload_form': upload_form}
    print(context)
    if upload_form.is_valid():
        print(context)
        upload_form.save()
        return render(request, 'post/frontpage.html', context)
    else:
        return render(request, 'post/frontpage.html', context)

def post_next(request, post_id):
    new_id = str(int(post_id)+1)



def post_prev(request, post_id):
    new_id = str(int(post_id)-1)
    try:
        post = Post.objects.get(pk=new_id)
        out = Comment.objects.filter(comment_post=new_id)
        post.post_views = getattr(post, 'post_views') + 1
        post.save()
        return render(request, 'post/detail.html', {'post': post, 'comment': out})
    except Post.DoesNotExist:
        raise Http404()


def user_post_like(request, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        p = Points_Post.objects.filter(points_post_post=post, points_post_user=request.user)

        if p.exists():
            like = p[0]
            if like.points_post_vote == 'D':
                like.points_post_vote = 'L'
                like.save()
                post.post_points += 2
                post.save()

            elif like.points_post_vote == 'N' or like.points_post_vote is None:
                like.points_post_vote = 'L'
                like.save()
                post.post_points += 1
                post.save()
        else:
            like = Points_Post(points_post_post=post, points_post_user=request.user, points_post_vote='L')
            like.save()
            post.post_points += 1
            post.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def user_post_dislike(request, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        p = Points_Post.objects.filter(points_post_post=post, points_post_user=request.user)

        if p.exists():
            like = p[0]
            if like.points_post_vote == 'L':
                like.points_post_vote = 'D'
                like.save()
                post.post_points -= 2
                post.save()

            elif like.points_post_vote == 'N' or like.points_post_vote is None:
                like.points_post_vote = 'D'
                like.save()
                post.post_points -= 1
                post.save()
        else:
            like = Points_Post(points_post_post=post, points_post_user=request.user, points_post_vote='L')
            like.save()
            post.post_points -= 1
            post.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def user_comment_like(request, post_id , comment_id):

    try:
        comment = Comment.objects.get(pk=comment_id)
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        c = Points_Comment.objects.filter(points_comment_comment=comment, points_comment_user=request.user,
                                          points_comment_post=post)

        if c.exists():
            like = c[0]
            if like.points_comment_vote == 'D':
                like.points_comment_vote = 'L'
                like.save()
                comment.comment_points += 2
                comment.save()
            elif like.points_comment_vote == 'N' or like.points_comment_vote is None:
                like.points_comment_vote = 'L'
                like.save()
                comment.comment_points += 1
                comment.save()
        else:
            like = Points_Comment(points_comment_post=post, points_comment_user=request.user, points_comment_vote='L',
                                  points_comment_comment=comment)
            like.save()
            comment.comment_points += 1
            comment.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def user_comment_dislike(request, post_id, comment_id):

    try:
        comment = Comment.objects.get(pk=comment_id)
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        c = Points_Comment.objects.filter(points_comment_comment=comment, points_comment_user=request.user,
                                          points_comment_post=post)

        if c.exists():
            like = c[0]
            if like.points_comment_vote == 'L':
                like.points_comment_vote = 'D'
                like.save()
                comment.comment_points -= 2
                comment.save()
            elif like.points_comment_vote == "N" or None:
                like.points_comment_vote = 'D'
                like.save()
                comment.comment_points -= 1
                comment.save()
        else:
            like = Points_Comment(points_comment_post=post, points_comment_user=request.user, points_comment_vote='D',
                                  points_comment_comment=comment)
            like.save()
            comment.comment_points -=1
            comment.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def user_comment_favorite(request, post_id, comment_id):

    try:
        comment = Comment.objects.get(pk=comment_id)
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        c = Points_Comment.objects.filter(points_comment_comment=comment, points_comment_user=request.user,
                                          points_comment_post=post)

        if c.exists():
            like = c[0]
            if like.points_comment_isFavorited == 'N' or like.points_comment_isFavorited is None:
                like.points_comment_isFavorited = 'Y'
                like.save()
                comment.comment_points += 5
                comment.comment_favorited += 1
                comment.save()
        else:
            like = Points_Comment(points_comment_post=post, points_comment_user=request.user, points_comment_vote='N',
                                  points_comment_comment=comment, points_comment_isFavorited='Y')
            like.save()
            comment.comment_points += 5
            comment.comment_favorited += 1
            comment.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def user_post_favorite(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        out = Comment.objects.filter(comment_post=post_id)
        p = Points_Post.objects.filter(points_post_post=post, points_post_user=request.user)

        if p.exists():
            like = p[0]
            if like.points_post_isFavorited == 'N' or like.points_post_isFavorited is None:
                like.points_post_isFavorited = 'Y'
                like.save()
                post.post_favorited += 1
                post.post_points += 5
                post.save()
        else:
            like = Points_Post(points_post_post=post, points_post_user=request.user, points_post_isFavorited='Y')
            like.save()
            post.post_favorited += 1
            post.post_points += 5
            post.save()

    finally:
        return render(request, 'post/detail.html', {'post': Post.objects.get(pk=post_id),
                                                    'comment': Comment.objects.filter(comment_post=post_id)})


def post_comment(request):

    if request.POST:
        comment = request.POST.get('comment_text', '')
        current_user = request.user
        post_id = request.POST.get('pk', '')
        post = Post.objects.get(pk=post_id)

        if comment is not "" or None :
            tmp = Comment(comment_text=comment, comment_user=current_user, comment_post=post)
            tmp.save()
            out = Comment.objects.filter(comment_post=post_id)
            return render(request, 'post/detail.html', {'post': post, 'comment': out})
