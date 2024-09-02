from django.db import models
import uuid


class Task(models.Model):
    """
    Represents a task submitted by a trainer and reviewed by a lead.
    """

    STATUS_CHOICES = [
        ("unclaimed", "Unclaimed"),
        ("in_progress", "In Progress"),
        ("in_review", "In Review"),
        ("completed", "Completed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique ID for the tasks.",
    )
    name = models.CharField(max_length=100, help_text="Name of the task.")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, help_text="Current status of the task."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when a member was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when a member was last updated."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ["name"]
