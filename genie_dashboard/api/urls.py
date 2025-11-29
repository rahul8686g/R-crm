"""
URL patterns for horilla_dashboard API
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from genie_dashboard.api.views import (
    ComponentCriteriaViewSet,
    DashboardComponentViewSet,
    DashboardFolderViewSet,
    DashboardViewSet,
)

router = DefaultRouter()
router.register(r"dashboard-folders", DashboardFolderViewSet)
router.register(r"dashboards", DashboardViewSet)
router.register(r"dashboard-components", DashboardComponentViewSet)
router.register(r"component-criteria", ComponentCriteriaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
