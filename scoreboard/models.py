from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=100)
    service_seconds = models.FloatField()

    def __str__(self):
        return f"{self.player_name} - {self.service_seconds}"
