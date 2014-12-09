#from django import http
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from foobarbaz.models import Foo

#def foo(request):
#    context = {
#        'jobs': Job.objects.all().order_by('-start'),
#        'skills': Skill.objects.all(),
#    }
#    return render(request, 'foo.html', context)

@login_required
def index(request):
    return render(request, 'index.html', {})

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login')
