from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI
from ninja.openapi.views import openapi_json, openapi_view
from ninja.security import APIKeyHeader

from food_api.api import router as food_api_router


class ApiKey(APIKeyHeader):
    param_name = settings.API_HEADER

    def authenticate(self, request, key):
        if key == settings.API_TOKEN:
            return key


header_key = ApiKey()

api = NinjaAPI(
    title=f"{settings.APP_NAME} API",
)


@staff_member_required
def authenticated_openapi_json(request):
    return openapi_json(request, api)


@staff_member_required
def authenticated_openapi_view(request):
    return openapi_view(request, api)


api.add_router("", food_api_router)
