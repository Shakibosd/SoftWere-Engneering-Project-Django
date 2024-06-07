import datetime
from django.db import models
from Musician.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='Album')
    # release_date = models.DateField()
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    release_date=models.DateField(default=datetime.date.today)  

    def __str__(self):
        return f"{self.name}"