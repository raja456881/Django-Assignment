from django.urls import path,include
from.import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", views.index, name="login"),
    path("sigup/", views.register, name="sigin"),
    path("login/", views.UserLoginView.as_view(), name="login1"),
    path("sighand", views.UserRegistrationView.as_view(), name="sigin1"),
    path("logout", views.handlelogout, name="logout"),
    path("profileviw", views.UserProfileView, name="profile")
]
