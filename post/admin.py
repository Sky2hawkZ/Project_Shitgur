from django.contrib import admin

from models import Post, Points_Comment, Points_Post, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Points_Comment)
admin.site.register(Points_Post)
