
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from organizer import urls as organizer_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(organizer_urls)),
    path("uploads/", include("creation.urls")),
    path("account/", include("account.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)