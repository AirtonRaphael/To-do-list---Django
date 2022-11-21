from django.db import models

# Create your models here.

class Task(models.Model):
    option = [
        ('O', 'Do'),
        ('E', 'Done')
    ]

    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(
        max_length=1,
        choices = option,
        default = 'O'
        )
    def __str__(self):
        return self.name
    
