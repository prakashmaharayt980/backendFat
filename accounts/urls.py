from django.urls import path
from .views import (
    RegisterView,
    ClientLoginView,
    AdminLoginView,
    LogoutView,
    UserProfileView,
    ChangePasswordView,

)
from .googlelogin import GoogleLoginAPIView
from .facebooklogin import FacebookLoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
  path("social/google/", GoogleLoginAPIView.as_view(), name="google-login"),
    path("social/facebook/", FacebookLoginAPIView.as_view(), name="facebook-login"),
    path("client/login/", ClientLoginView.as_view(), name="client-login"),
    path("admin/login/", AdminLoginView.as_view(), name="admin-login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
