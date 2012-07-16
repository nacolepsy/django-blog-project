#from django.contrib import admin
from django.db import models
from django.contrib import admin
import re
# Create your models here.

class Category(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField()
	def __unicode__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	def __unicode__(self):
		return self.name	

class Post(models.Model):
	title= models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	author=models.CharField(max_length=50)
	body_text = models.TextField()
	created_date = models.DateField()
	author = models.ManyToManyField(Author)
	update_date = models.DateField()	
	def __unicode__(self):
		return self.title
	def limitpost(self):
		return self.body_text[:60]
	def get_absolute_url(self):
		return "/blog/posts/%i/true" % self.id
"""
	@models.permalink
	def get_absolute_url(self):
		return ('body',(),
			{'id':self.id,'showComments':'true/'})

"""

class Comments(models.Model):
	author=models.CharField(max_length=50)
	comment_date=models.DateField()
	post=models.ForeignKey(Post)
	body=models.TextField()
	def __unicode__(self):
		return self.body
	def limitcomment(self):
		return self.body[:60]

class CommentInline(admin.TabularInline):
	model=Comments
	
class CommentAdmin(admin.ModelAdmin):
	list_display =('post','author','comment_date','limitcomment',)
	list_filter=('comment_date','author',)



class PostAdmin(admin.ModelAdmin):
	
	list_display = ('title','created_date','update_date',)
	list_filter = ('created_date',)
	search_fields = ('title',)
	ordering = ('title',)
	inlines = [CommentInline] 	

	"""
	class title_first_10(self):
		return self.title[:10]
	list_display = ('title_first_10',)
	"""
		#class Admin:
		#	pass
	



class Reply(models.Model):
	reply_date=models.DateField()
	author=models.ForeignKey(Author)
        comment=models.ManyToManyField(Comments)
	body=models.TextField()
	def __unicode__(self):
		return self.body



	
"""
		title = models.CharField(max_length=100)
		date_created = models.DateField()
		date_updated = models.DateField()
		search = models.DateField()
	def __unicode__(self):
		return self.title
"""
