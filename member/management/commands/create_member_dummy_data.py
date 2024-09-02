from django.core.management.base import BaseCommand
from member.models import Member
import random


class Command(BaseCommand):
    help = "Create dummy data for Member model"

    def handle(self, *args, **kwargs):
        roles = ["trainer", "lead"]
        for i in range(5):
            role = random.choice(roles)
            Member.objects.create(
                role=role,
                email=f"user{i}@turing.com",
                full_name=f"User {i}",
            )
