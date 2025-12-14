from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.db import DatabaseError

class BaseBlogAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            return Response(
                {"error": exc.detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        if isinstance(exc, DatabaseError):
            return Response(
                {"error": "Database error occurred."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"error": "Unexpected error occurred.", "details": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
