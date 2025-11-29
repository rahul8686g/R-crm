"""Admin configuration for the leads app in Horilla CRM."""

from auditlog.models import LogEntry
from django.contrib import admin

# Ensure idempotent registration
from .models import EmailToLeadConfig, Lead, LeadStatus

if Lead not in admin.site._registry:
    admin.site.register(Lead)
if LeadStatus not in admin.site._registry:
    admin.site.register(LeadStatus)
admin.site.unregister(LogEntry)
if EmailToLeadConfig not in admin.site._registry:
    admin.site.register(EmailToLeadConfig)


@admin.register(LogEntry)
class CustomLogEntryAdmin(admin.ModelAdmin):
    """Custom admin for LogEntry to display relevant fields."""

    list_display = ("object_repr", "content_type", "action", "actor", "timestamp")
    list_filter = ("content_type", "action", "actor", "timestamp")
    search_fields = ("object_repr", "changes", "actor__username")
