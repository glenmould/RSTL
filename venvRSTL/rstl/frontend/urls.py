from django.urls import path
from . import views
#from . views import AboutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    #    path('about/', views.about, name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('travelservices/', views.TravelservicesView.as_view(), name='travelservices'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),

]

urlpatterns += staticfiles_urlpatterns()
