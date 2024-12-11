from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

schemas_view = get_schema_view(
    openapi.Info(
        title="Expense Tracker API",
        default_version="v1",
        description="API for managing expenses and transactions"
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("expenses.urls")),

    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += [
    path('docs/', schemas_view.with_ui('swagger', cache_timeout=0), name="swagger-ui")
]

