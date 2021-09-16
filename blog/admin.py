from django.contrib import admin
from .models import Comment, Article, Subject

admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Article)
