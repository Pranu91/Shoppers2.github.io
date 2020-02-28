
from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def blogpost(request,id):
     #us side wali models m se le aegi us no ki chize post_id m se

    return render(request, 'blog/blogpost.html')