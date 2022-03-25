from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=25, unique=True)
    is_done = models.BooleanField(default=False)
    description = models.CharField(max_length=200, default="No Description")
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return 'task/' + str(self.id)


