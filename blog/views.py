
from django.shortcuts import render
from django.utils import timezone
from .models import Soccer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms import SoccerForm, CommentForm
from .models import Soccer, Comment



def soccer_list(request):
    posts = Soccer.objects.all()
    return render(request, 'blog/soccer_list.html', {'posts': posts})


def soccer_detail(request, pk):
    post = get_object_or_404(Soccer, pk=pk)
    return render(request, 'blog/soccer_detail.html', {'soccer': post})

@login_required
def soccer_new(request):
    if request.method == "POST":
        form = SoccerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('blog:soccer_detail', pk=post.pk)
    else:
        form = SoccerForm()
    return render(request, 'blog/soccer_edit.html', {'form': form})

@login_required
def soccer_edit(request, pk):
    post = get_object_or_404(Soccer, pk=pk)
    if request.method == "POST":
        form = SoccerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('blog:soccer_detail', pk=post.pk)
    else:
        form = SoccerForm(instance=post)
    return render(request, 'blog/soccer_edit.html', {'form': form})

@login_required
def soccer_remove(request, pk):
    post = get_object_or_404(Soccer, pk=pk)
    post.delete()
    return redirect('blog:soccer_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Soccer, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.soccer = post
            comment.save()
            return redirect('blog:soccer_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:soccer_detail', pk=comment.soccer.pk)
