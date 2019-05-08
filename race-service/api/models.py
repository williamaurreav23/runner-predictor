from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    distance = models.DecimalField(
        max_digits=10, decimal_places=1, null=True, blank=True
    )
    elevation_gain = models.PositiveIntegerField(null=True, blank=True)
    elevation_lost = models.PositiveIntegerField(null=True, blank=True)
    itra = models.PositiveIntegerField(null=True, blank=True)
    food_point = models.PositiveIntegerField(null=True, blank=True)
    time_limit = models.DecimalField(
        max_digits=10, decimal_places=1, null=True, blank=True
    )

    class Meta:
        ordering = ["-start_date"]
        verbose_name_plural = "races"
        unique_together = ["name", "start_date"]

    def __str__(self):
        return f"{self.name} {self.start_date}"

    @property
    def elevation_diff(self):
        """Calculating difference between elevation gain and lost"""
        if not self.elevation_gain or not self.elevation_lost:
            return None
        return self.elevation_gain - self.elevation_lost