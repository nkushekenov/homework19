from operator import index
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include

def redirect_to_user_list(request):
    return HttpResponseRedirect('/users/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_user_list),
    path('', include('HW19.urls')),
    path('', index, name='home'),
]
