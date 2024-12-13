from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path("", RedirectView.as_view(url="/api/docs/", permanent=True)),
    path("admin/", admin.site.urls),
    path("api/", include("expenses.urls")),
    path(
        "api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
