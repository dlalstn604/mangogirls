from django.shortcuts import render

# Create your views here.

def soccer_list(request):
    return render(request, 'blog/soccer_list.html', {})