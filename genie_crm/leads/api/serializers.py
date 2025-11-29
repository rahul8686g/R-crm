"""
Serializers for horilla_crm.leads models
"""

from rest_framework import serializers

from genie_core.api.serializers import HorillaUserSerializer
from genie_crm.leads.models import Lead, LeadStatus


class LeadStatusSerializer(serializers.ModelSerializer):
    """Serializer for LeadStatus model"""

    class Meta:
        model = LeadStatus
        fields = "__all__"
