from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'blog/index.html'
    ##context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template)

def detail(request):
    template = 'blog/detail.html'
    return render(request, template)

def category(request):
    template = 'blog/categroy.html'
    return render(request, template)
