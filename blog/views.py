# Create your views here.
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comments 


def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))


def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		exclude=['post']



@csrf_exempt
def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    comment=Comments.objects.filter(post=id)
    if request.method == 'POST':
	comment = Comments(post=post)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
	      form.save()
	return HttpResponseRedirect(request.path)
    else:
	 form = CommentForm()
    
    t = loader.get_template('blog/post_detail.html') 
    c = Context({'posts':post, 'comments':comment,'form' : form})
    return HttpResponse(t.render(c))


def edit_comment(request, id):
	edit = Comments.objects.get(pk=id)
	t = loader.get_template('blog/edit_comment.html')
	c = Context({'posts':edit })
	return HttpResponse(t.render(c))

	#HttpResponseRedirect(get_absolute_url())

	

    
def post_search(request,  mysearch):
    searchtxt = Post.objects.filter(body_text__contains=str(mysearch))
    t = loader.get_template('blog/post_search.html')
    c = Context({'post':searchtxt, 'word':mysearch })
    return HttpResponse(t.render(c))
    


def home(request):
    return render_to_response('blog/base.html',{})

