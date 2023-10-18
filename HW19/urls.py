from django import views
from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]
