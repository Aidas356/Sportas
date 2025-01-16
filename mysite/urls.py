from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
                  path('web/', include('web.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', RedirectView.as_view(url='web/', permanent=True)),
              ] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))