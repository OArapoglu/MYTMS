from django.core.management.base import BaseCommand
from task.models import Task
import random
import uuid


class Command(BaseCommand):
    help = "Create dummy data for Task model"

    def handle(self, *args, **kwargs):
        statuses = ["unclaimed", "in_progress", "in_review", "completed"]
        for i in range(5):
            Task.objects.create(
                name=f"Task {uuid.uuid4()}",
                status=random.choice(statuses),
            )
