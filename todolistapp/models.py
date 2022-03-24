from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return 'task/' + str(self.id)
