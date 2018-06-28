from django.shortcuts import render
from django.utils import timezone
from .models import Soccer

# Create your views here.

def post_list(request):
    posts = Soccer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/soccer_list.html', {})
