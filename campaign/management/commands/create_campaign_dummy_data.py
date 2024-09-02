from django.core.management.base import BaseCommand
from campaign.models import Campaign
import uuid


class Command(BaseCommand):
    help = "Create dummy data for Campaign model"

    def handle(self, *args, **kwargs):
        for i in range(5):
            Campaign.objects.create(name=f"Campaign {uuid.uuid4()}")
