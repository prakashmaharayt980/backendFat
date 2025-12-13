from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from products.models import Product, Category
from emi.models import EMIApplication
from blog.models import BlogPost
from django.db.models import Sum

class DashboardStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_products = Product.objects.count()
        total_orders = 0 # Placeholder if no Order model yet
        total_emi_applications = EMIApplication.objects.count()
        pending_emi = EMIApplication.objects.filter(status='pending').count()
        active_emi = EMIApplication.objects.filter(status='active').count()
        total_blogs = BlogPost.objects.count()

        # Calculate revenue/value if possible
        total_emi_value = EMIApplication.objects.filter(status='active').aggregate(Sum('total_amount'))['total_amount__sum'] or 0

        return Response({
            "stats": {
                "total_products": total_products,
                "total_orders": total_orders,
                "total_emi_applications": total_emi_applications,
                "pending_emi": pending_emi,
                "active_emi": active_emi,
                "total_blogs": total_blogs,
                "total_emi_value": total_emi_value
            },
            "recent_activity": [] # Add recent logs or actions here
        })
