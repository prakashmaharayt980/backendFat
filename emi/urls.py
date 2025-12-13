from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EMIApplicationViewSet, BankViewSet

router = DefaultRouter()
router.register(r'applications', EMIApplicationViewSet)
router.register(r'banks', BankViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
