from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MemberViewSet

router = DefaultRouter()
router.register(r"", MemberViewSet, basename="member")

urlpatterns = [
    path("", include(router.urls)),
]
