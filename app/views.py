from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Path, Comment, Image

from .forms import CommentForm, PathFormWithImages

import sys

def index(request):

    paths = Path.objects.all()

    for path in paths:
        path.image = Image.objects.filter(path=path).first()
        comments = Comment.objects.filter(path=path).all()
        path.note = avg_note(comments)

    context = {'paths': paths}

    return render(request, 'app/index.html', context)

def detail(request, path_id):

    try:
        # First load the path and images/comments associated to pass in context
        path = Path.objects.get(pk=path_id)
        comments = Comment.objects.filter(path=path).all()
        images = Image.objects.filter(path=path).all()

    except Path.DoesNotExist:
        raise Http404("Path does not exist.")

    if request.method == 'POST':

        # Create a mutable copy of the request to insert the path
        # Because I didn't find a way to change the form after initialized with the posted data.
        post = request.POST.copy()
        post['path'] = path

        form = CommentForm(post)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('app:detail', kwargs={'path_id': path.id}))

    else:
        form = CommentForm()

    # Compute average note from all comments
    path.note = avg_note(comments)    
    return render(request, 'app/detail.html', {'path': path, 'comments': comments, 'images': images, 'form': form})


def new_path(request):
    
    if request.method == 'POST':

        form = PathFormWithImages(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')

        if form.is_valid():

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            path = Path.objects.create(name=name, description=description)
            path.save()
            
            for f in files:
                image = Image.objects.create(path=path, image=f)
                image.save()
            
            return HttpResponseRedirect(reverse('app:detail', kwargs={'path_id': path.id}))

        else:
            return render(request, 'app/new_path.html', {'images': files, 'form': form})

    else:
        form = PathFormWithImages()
        return render(request, 'app/new_path.html', {'form': form})



def avg_note(comments):
    # Just average note of all comments
    
    if len(comments) != 0:
        avg = 0
        for comment in comments:
            avg += comment.note
        return round(avg / len(comments), 1)
    return '?'