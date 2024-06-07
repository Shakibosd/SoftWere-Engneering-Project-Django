
from django.db import models


class Musician(models.Model):
    INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('piano', 'Piano'),
        ('drums', 'Drums'),
        ('violin', 'Violin'),
        ('saxophone', 'Saxophone'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'