from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import SoccerForm
from .models import Soccer

def soccer_list(request):
    posts = Soccer.objects.all()
    return render(request, 'blog/soccer_list.html', {'posts': posts})


def soccer_detail(request, pk):
    post = get_object_or_404(Soccer, pk=pk)
    return render(request, 'blog/soccer_detail.html', {'post': post})


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