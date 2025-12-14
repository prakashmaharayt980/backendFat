from django.shortcuts import render

# Create your views here.
from payments.exception import BasePaymentAPIView
from payments.serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment
from django.shortcuts import get_object_or_404
from payments.pagination import PaymentsPagination


class CreatePaymentAPIView(BasePaymentAPIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetAllPaymentsAPIView(BasePaymentAPIView):
    def get(self, request):
        payments = Payment.objects.all().order_by('-created_at')
        paginator = PaymentsPagination()
        page = paginator.paginate_queryset(payments,request)
        serializer = PaymentSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class GetPaymentByIdAPIView(BasePaymentAPIView):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        return Response(PaymentSerializer(payment).data)

class UpdatePaymentAPIView(BasePaymentAPIView):
    def put(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeletePaymentAPIView(BasePaymentAPIView):
    def delete(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
