"""App configuration for dashboard app."""

from django.apps import AppConfig
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class HorillaDashboardConfig(AppConfig):
    """
    HorillaDashboardConfig App Configuration
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "genie_dashboard"
    label = "horilla_dashboard"
    verbose_name = _("Dashboard")

    # def get_api_paths(self):
    #     """
    #     Return API path configurations for this app.

    #     Returns:
    #         list: List of dictionaries containing path configuration
    #     """
    #     return [
    #         {
    #             'pattern': 'crm/horilla_dashboard/',
    #             'view_or_include': 'horilla_dashboards.api.urls',
    #             'name': 'horilla_crm_dashboards_api',
    #             'namespace': 'horilla_crm_dashboards'
    #         }
    #     ]

    def ready(self):
        # try:
        # Auto-register this app's URLs and add to installed apps
        from django.urls import include, path

        from genie.urls import urlpatterns

        # Add app URLs to main urlpatterns
        urlpatterns.append(
            path("dashboard/", include("genie_dashboard.urls")),
        )

        __import__("genie_dashboard.menu")
        __import__("genie_dashboard.signals")
        # except Exception as e:
        #     import logging

        #     logging.warning("HorillaDashboardConfig.ready failed: %s", e)
        super().ready()
