from django.shortcuts import render_to_response
from .models import Post
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


from forms import SignUpForm

# Create your views here.


def index(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    activa_index = True
    return render_to_response('base.html',{'posts':posts,'activa_index':activa_index},
                              context_instance=RequestContext(request))
@login_required()
def profile(request):
    profile = True
    return render_to_response('profile.html', {'profile':profile},context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html',context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/profile")
        else:
            return HttpResponseRedirect("/invalid")
    else:
        return render_to_response('registration/login.html', {'signup':'login'},context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def invalid(request):
    return render_to_response('404/incorrecto.html',
                              context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            # user.first_name = first_name
            # user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect('/thanks')  # Redirect after POST
        else:
            print 'no ha pasado la validacion'
    else:
        form = SignUpForm()

    signup='signup'
    data = {
        'form': form,
        'signup': signup
    }
    return render_to_response('registration/signup.html', data, context_instance=RequestContext(request))