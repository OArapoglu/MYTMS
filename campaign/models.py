from django.db import models
import uuid


class Campaign(models.Model):
    """
    Represents a campaign.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique ID for the campaigns.",
    )
    name = models.CharField(max_length=100, help_text="Name of the campaign.")
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when a member was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when a member was last updated."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Campaigns"
        ordering = ["name"]
