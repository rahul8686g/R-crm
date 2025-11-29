"""
URL patterns for horilla_crm.campaigns API
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from genie_crm.campaigns.api.views import CampaignViewSet

router = DefaultRouter()
router.register(r"campaigns", CampaignViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
