from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'blog/index.html'
    ##context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template)

def post_detail(request, id):
    template = 'blog/detail.html'
    return render(request, template)

def category_post(request, category_slug):
    template = 'blog/category.html'
    return render(request, template)
