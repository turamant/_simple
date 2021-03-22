from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)