from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import GalleryPost
# Create your views here.

def index(request):
    all_galleryposts = GalleryPost.objects.all()
    context = {'all_galleryposts': all_galleryposts}
    return render(request, 'post/frontpage.html', context)

def detail(request, post_id):
    # gallerypost = GalleryPost.objects.get(pk=post_id)
    gallerypost = get_object_or_404(GalleryPost, pk=post_id)
    return render(request, 'post/detail.html', context), {'gallerypost': gallerypost}
