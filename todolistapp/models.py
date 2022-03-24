from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return 'list/' + str(self.id)

    
    
class Task(models.Model):
    list = models.ForeignKey(List, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    date_scheduled = models.DateField(auto_now_add=True)
    date_due = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

