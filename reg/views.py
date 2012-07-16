# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
#11

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
	#uname=request.Post['username']
	#pas=  request.Post['password']
	user= authenticate(username=request.POST['username'], password=request.POST['password'])
	
	if user is not None:
		if user.is_active:		
			login(request, user)
			form = LoginForm()
			#return HttpResponseRedirect('/reg/login/')
			
			return render_to_response('reg/login.html', {'form': form,'logged_in': request.user.is_authenticated()})
		  	#return render_to_response('blog/post_list.html', {'form': form,'logged_in': request.user.is_authenticated()})
#24 		
		else:
			return render_to_response('reg/error')
    form = LoginForm()
    return render_to_response('reg/login.html', {'form': form,'logged_in': request.user.is_authenticated()})

@csrf_exempt
def do_logout(request):
    logout(request)
    
    return render_to_response('reg/logout.html')
def do_error(request):
    return render_to_response('reg/error.html')
#34
