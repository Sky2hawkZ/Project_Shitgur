# -*- coding: utf-8 -*-
from django import forms
from post.models import Post

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_text','post_tags','post_posted','post_image')
