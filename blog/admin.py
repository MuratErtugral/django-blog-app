from django.contrib import admin
from .models import Category, Like, Post ,Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
