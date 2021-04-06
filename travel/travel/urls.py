from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_.urls')),
    path('core/', include('core.urls')),
    path('shop/', include('shop.urls')),
    path('payment/', include('payment.urls')),
    path('feedback/', include('feedback.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
