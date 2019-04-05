from django.shortcuts import render

# Create your views here.

def Team_List(request):
    return render(request, 'blog/Team_List.html', {})