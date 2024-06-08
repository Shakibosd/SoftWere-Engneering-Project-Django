from django.db import models
from task.models import TaskModel

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
