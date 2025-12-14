from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError, IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny


class BaseAPIView(APIView):
    permission_classes = [AllowAny]

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            return Response(
                {"error": exc.detail},
                status=status.HTTP_400_BAD_REQUEST
            )

        if isinstance(exc, IntegrityError):
            return Response(
                {"error": "Database integrity error."},
                status=status.HTTP_409_CONFLICT
            )

        if isinstance(exc, DatabaseError):
            return Response(
                {"error": "Database error occurred."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"error": "An unexpected error occurred.", "details": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
