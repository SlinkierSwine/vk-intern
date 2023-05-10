from django.urls import path
from . import views


urlpatterns = [
    path('users/<int:id>', views.UserDetail.as_view()),
    path('', views.ProfileList.as_view()),
    path('create', views.ProfileCreateAPIView.as_view()),
    path('<int:id>', views.ProfileDetail.as_view()),
    path('<int:profile_id>/friends', views.FriendListAPIView.as_view()),
    path('friend-status', views.FriendStatusAPIView.as_view()),
    path('delete-friend', views.DeleteFriendAPIView.as_view()),
]

