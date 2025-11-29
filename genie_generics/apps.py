from django.apps import AppConfig


class HorillaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "genie_generics"
    label = "horilla_generics"

    def ready(self):
        try:
            # Auto-register this app's URLs and add to installed apps
            from django.urls import include, path

            import genie_generics.signals
            from genie.urls import urlpatterns

            urlpatterns.append(
                path(
                    "generics/",
                    include("genie_generics.urls", namespace="horilla_generics"),
                ),
            )

        except Exception as e:
            import logging

            logging.warning(f"HorillaConfig.ready failed: {e}")
            pass

        super().ready()
