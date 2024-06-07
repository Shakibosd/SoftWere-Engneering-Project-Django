from django.db import models
    

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_complited = models.BigIntegerField(default=True)
    task_assign_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle    