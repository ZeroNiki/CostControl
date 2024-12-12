from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, TransactionViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("transactions", TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegistrationViewSet.as_view(), name="user-registration"),
]
