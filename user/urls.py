from django.urls import path
from . import views


urlpatterns = [
    path('users/<int:id>', views.UserDetail.as_view()),
    path('', views.ProfileList.as_view()),
    path('<int:id>', views.ProfileDetail.as_view()),
    path('<int:profile_id>/friends', views.FriendListAPIView.as_view()),
]

