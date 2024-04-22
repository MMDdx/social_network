from django.urls import path
from .views import UserListView,RequestView,RequestListView, AcceptRequestView,FriendsView
urlpatterns = [
    path('users-list/', UserListView.as_view()),
    path('friendships/request/', RequestView.as_view()),
    path('friendships/request-list/',RequestListView.as_view()),
    path('friendships/accept/', AcceptRequestView.as_view()),
    path('friendships/friends/',FriendsView.as_view()),



]