from rest_framework import serializers
from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    """
    Serializer for the Campaign model.
    """

    class Meta:
        model = Campaign
        fields = "__all__"
