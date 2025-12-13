from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


# ------------------------ HELPER ------------------------
def get_jwt_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "user": UserSerializer(user).data
    }


# ------------------------ REGISTER ------------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


# ------------------------ CLIENT LOGIN ------------------------
class ClientLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password required"}, status=400)

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=401)

        if user.is_staff:
            return Response({"detail": "Admins must use admin login API"}, status=403)

        return Response(get_jwt_for_user(user), status=200)


# ------------------------ ADMIN LOGIN ------------------------
class AdminLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password required"}, status=400)

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=401)

        if not user.is_staff:
            return Response({"detail": "You are not allowed to login as admin"}, status=403)

        return Response(get_jwt_for_user(user), status=200)


# ------------------------ GOOGLE LOGIN ------------------------
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.sociallogin.user  # Corrected
        if not user.is_staff:
            return Response(get_jwt_for_user(user), status=200)
        return Response({"detail": "Admins cannot login here"}, status=403)


# ------------------------ FACEBOOK LOGIN ------------------------
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.sociallogin.user
        if not user.is_staff:
            return Response(get_jwt_for_user(user), status=200)
        return Response({"detail": "Admins cannot login here"}, status=403)


# ------------------------ LOGOUT ------------------------
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)

        return Response({"detail": "Logout successful"}, status=200)


# ------------------------ PROFILE ------------------------
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# ------------------------ CHANGE PASSWORD ------------------------
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response({"detail": "Password changed successfully."}, status=200)
