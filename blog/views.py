# Create your views here.
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comments 

#10

def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		exclude=['post','author']
		
		


@csrf_exempt
def post_detail(request, id, showComments=False):
    if not request.user.is_authenticated():
       	return HttpResponseRedirect('/reg/login/')
	#return HttpResponseRedirect('/reg/login/?next=/blog/post_list%s' % request.path)
    else:
	post=Post.objects.filter(pk=id)
	comment=Comments.objects.filter(post=id)
	for p in post:
            wanted_post=p
	if request.method == 'POST':
	    comment = Comments(post=wanted_post)
	    comment.author= request.user
	    form = CommentForm(request.POST, instance=comment)
	    if form.is_valid():
		form.save()
		return HttpResponseRedirect(request.path)
	else:
	    form = CommentForm()
	    
	    t = loader.get_template('blog/post_detail.html') 
	    c = Context({'posts':post, 'comments':comment,'form' : form,'user':request.user})
	    return HttpResponse(t.render(c))


@csrf_exempt
def edit_comment(request, id):
	edit = Comments.objects.get(pk=id)
	
    	if request.method == 'POST':
		#edit = Comments(post=edit)
        	form = CommentForm(request.POST, instance=edit)
        	if form.is_valid():
			form.save()
		return HttpResponseRedirect(edit.post.get_absolute_url())
	else:
		form = CommentForm(instance=edit)
#60
	t = loader.get_template('blog/edit_comment.html')
	c = Context({'posts':edit, 'form' : form })
	return HttpResponse(t.render(c))
"""	
311 unsub
"""
def my_view(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('reg/login/?next=%s' % request.path)
    
def post_search(request,  mysearch):
    searchtxt = Post.objects.filter(body_text__contains=str(mysearch))
    t = loader.get_template('blog/post_search.html')
    c = Context({'post':searchtxt, 'word':mysearch })
    return HttpResponse(t.render(c))
   


def home(request):
    return render_to_response('blog/base.html',{})

