from django.views import View
from django.http import HttpResponse
from .models import User
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'HW19/user_list.html', {'users': users})


class UserDetailView(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            return render(request, 'HW19/user_detail.html', {'user': user})
        return HttpResponse("No user id provided.")
    
class UserDetailView(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        context = {'user': user}
        return render(request, 'HW19/user_detail.html', context)
