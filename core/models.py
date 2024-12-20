from django.db import models
from django.conf import settings


class Quota(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quota')
    total_time = models.FloatField(default=0.0, help_text="Total audio processing time in seconds.")
    limit = models.FloatField(default=3600.0, help_text="Maximum allowed audio processing time in seconds (default: 1 hour).")

    def can_process(self, time_to_process):
        """
        Check if the user can process the given amount of time without exceeding their limit.
        """
        return (self.total_time + time_to_process) <= self.limit

    def add_time(self, time_to_add):
        """
        Add processing time to the user's quota if it doesn't exceed the limit.
        """
        if self.can_process(time_to_add):
            self.total_time += time_to_add
            self.save()
            return True
        return False

    def reset_quota(self):
        """
        Reset the user's quota.
        """
        self.total_time = 0.0
        self.save()

    def __str__(self):
        return f"{self.user.email} - {self.total_time}/{self.limit} seconds used"
