from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from blog.forms import PostingForm
from blog.forms import LoginForm
from blog.models import Posting

def list_postings(request, id='0'):
    #postings = cache.get('postings')
    #if postings is None:
    #    postings = Posting.objects.all().order_by('-date')[:10]
    #    cache.add('postings', postings)
    postings = Posting.objects.all().order_by('-date')[:11]
    form = LoginForm()
    return render(request, 'index.html',
        {'postings': postings, 'form': form})

@login_required()
def show_form(request, id='0'):
    form = PostingForm()
    if id != '0':
        posting = Posting.objects.get(id=id)
        form = PostingForm(instance=posting)
    return render(request, 'form.html', {'form': form})

@login_required()
def update_posting(request, id='0'):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if id != '0':
            posting = Posting.objects.get(id=id)
            form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.save()
            #cache.delete('postings')
    return HttpResponseRedirect('/')

@login_required()
def delete_posting(request, id):
    posting = Posting.objects.get(id=id)
    posting.delete()
    #cache.delete('postings')
    return HttpResponseRedirect('/')

def log_user_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect('/')
