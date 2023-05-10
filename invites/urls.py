from django.urls import path
from . import views


urlpatterns = [
        path('<int:id>', views.InviteDetail.as_view()),
        path('from-user/<int:profile_id>', views.InviteFromUserAPIView.as_view()),
        path('to-user/<int:profile_id>', views.InviteToUserAPIView.as_view()),
        path('invite-user/', views.InviteUserAPIView.as_view()),
]

