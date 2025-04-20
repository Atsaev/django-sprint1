from django.shortcuts import render

# Create your views here.
def about(request):
    template = 'pages/about.html'
    ##context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template)

def rules(request):
    template = 'pages/rules.html'
    ##context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template)
