from rest_framework import viewsets, permissions
from .models import MenuSection
from .serializers import MenuSectionSerializer

class NavigationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that provides the navigation structure.
    """
    queryset = MenuSection.objects.all().prefetch_related('columns__items')
    serializer_class = MenuSectionSerializer
    permission_classes = [permissions.AllowAny]
