from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, 'index.html')

#def about(request):
#    return render(request, 'about.html')


class AboutView(generic.ListView):
    template_name = 'about.html'

    def get_queryset(self):
    	return None


class TravelservicesView(generic.ListView):
    template_name = 'travelservices.html'

    def get_queryset(self):
    	return None


class ContactView(generic.ListView):
    template_name = 'contact.html'

    def get_queryset(self):
    	return None


class BlogView(generic.ListView):
    template_name = 'blog.html'

    def get_queryset(self):
    	return None
