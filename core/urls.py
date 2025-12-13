from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NavigationViewSet
from .views_admin import DashboardStatsView

router = DefaultRouter()
router.register(r'navigation', NavigationViewSet, basename='navigation')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
]

