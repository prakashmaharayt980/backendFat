from django.urls import path
from . import views

urlpatterns = [

    path('getAllPayments/', views.GetAllPaymentsAPIView.as_view(), name='payment-list'),
    path('create/', views.CreatePaymentAPIView.as_view(), name='payment-create'),
    path('findById/<int:pk>/', views.GetPaymentByIdAPIView.as_view(), name='payment-detail'),
    path('update/<int:pk>/', views.UpdatePaymentAPIView.as_view(), name='payment-update'),
    path('delete/<int:pk>/', views.DeletePaymentAPIView.as_view(), name='payment-delete'),
]
