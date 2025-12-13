import requests
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class FacebookLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        access_token = request.data.get("access_token")
        password = request.data.get("password")  # Optional, for first-time set
        phone = request.data.get("phone")        # Optional, for first-time set
        address = request.data.get("address")    # Optional, for first-time set

        if not access_token:
            return Response({"error": "Access token is missing"}, status=400)

        # Verify token with Facebook Graph API
        url = f"https://graph.facebook.com/me?fields=id,name,email&access_token={access_token}"
        response = requests.get(url)

        if response.status_code != 200:
            return Response({"error": "Invalid token", "details": response.json()}, status=400)

        user_info = response.json()
        email = user_info.get("email")
        name = user_info.get("name")

        if not email:
            return Response({"error": "Facebook account does not provide an email"}, status=400)

        user, created = User.objects.get_or_create(email=email, defaults={"name": name})

        # Determine first login or old login
        first_login = created or not user.password or not user.phone

        # Check for missing required info
        missing_info = {}
        if not user.password or created:
            if not password:
                missing_info["password"] = "Password is required for first-time login"
            else:
                user.password = make_password(password)
        if not user.phone:
            if not phone:
                missing_info["phone"] = "Phone number is required for first-time login"
            else:
                user.phone = phone
        
        if address:
            user.address = address

        user.save()

        if missing_info:
            return Response({
                "message": "Additional information required",
                "logged_in": "new",
                "missing_fields": missing_info,
                "user": {
                    "email": user.email,
                    "name": user.name,
                    "phone": user.phone,
                    "address": user.address,
                }
            }, status=200)

        # All required info present → generate JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "message": "User logged in successfully",
            "logged_in": "old" if not first_login else "new",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "phone": user.phone,
                "address": user.address,
            }
        }, status=200)
