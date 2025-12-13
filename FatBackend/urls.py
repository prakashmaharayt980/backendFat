from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('products.urls')),
    path('blog/',include('blog.urls')),
    path('secure-admin/', admin.site.urls),
    # path('api/inventory/', include('inventory.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serving media files in development
