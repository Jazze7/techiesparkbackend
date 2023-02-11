from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls", namespace="web")),
    path('users/', include("users.urls", namespace="users")),
    path('accounts/', include('registration.backends.default.urls')),
    path("api/v1/events/",include("api.v1.events.urls")),
    path("api/v1/auth/",include("api.v1.auth.urls"))
    
    
]
if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)


    )
