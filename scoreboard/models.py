from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=100)
    survive_seconds = models.FloatField()

    def __str__(self):
        return f"{self.player_name} - {self.survive_seconds}"
