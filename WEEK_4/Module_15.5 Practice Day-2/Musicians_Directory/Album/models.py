from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=True)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.name    
    

    