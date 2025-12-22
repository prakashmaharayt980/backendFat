from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,AllowAny
from django.db import DatabaseError
from rest_framework.exceptions import ValidationError
import logging


logger = logging.getLogger('django')

class BasePaymentAPIView(APIView):
    permission_classes = [AllowAny,]

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            logger.error(str(exc),exc_info=True)
            return Response({"error": exc.detail}, status=status.HTTP_400_BAD_REQUEST)

        if isinstance(exc, DatabaseError):
            logger.error(str(exc),exc_info=True)
            return Response(
                {"error": "Database error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

        logger.error(str(exc),exc_info=True)
        return Response(
            {"error": "Unexpected error", "details": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
