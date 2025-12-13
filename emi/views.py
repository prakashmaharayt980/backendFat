from rest_framework import viewsets, permissions
from .models import EMIApplication, Bank
from .serializers import EMIApplicationSerializer, EMIApplicationDetailSerializer, BankSerializer

class EMIApplicationViewSet(viewsets.ModelViewSet):
    queryset = EMIApplication.objects.all()
    filterset_fields = ['status', 'email']
    search_fields = ['application_no', 'customer_name', 'phone']
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return EMIApplicationDetailSerializer
        return EMIApplicationSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()] # Allow anyone to apply
        return [permissions.IsAuthenticated()] # Only admin/staff can list/view/edit

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
