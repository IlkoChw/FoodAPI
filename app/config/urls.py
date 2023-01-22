from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .api import api, authenticated_openapi_json, authenticated_openapi_view


urlpatterns = [
    path('', admin.site.urls),
    path("api/docs", authenticated_openapi_view, name="docs"),
    path("api/openapi.json", authenticated_openapi_json, name="openapi-json"),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
