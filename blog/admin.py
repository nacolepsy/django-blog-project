from django.db import models
from blog.models import Category
from blog.models import Author
from blog.models import Post
from blog.models import Comments 
from blog.models import Reply 
from blog.models import PostAdmin
from blog.models import CommentAdmin

from django.contrib import admin
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Reply)


