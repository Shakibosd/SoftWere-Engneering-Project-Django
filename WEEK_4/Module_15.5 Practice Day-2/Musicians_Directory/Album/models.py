from django.db import models
from musician.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.name
