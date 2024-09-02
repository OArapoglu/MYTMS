from django.db import models


class Member(models.Model):
    """
    Represents a member, either a trainer or a lead.
    """

    ROLE_CHOICES = [
        ("trainer", "Trainer"),
        ("lead", "Lead"),
    ]

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, help_text="Role of the member."
    )
    email = models.EmailField(
        primary_key=True, help_text="Email address of the member."
    )
    full_name = models.CharField(max_length=100, help_text="Full name of the member.")
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when a member was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when a member was last updated."
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Members"
        ordering = ["full_name"]
