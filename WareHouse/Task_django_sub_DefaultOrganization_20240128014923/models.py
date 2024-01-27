'''
This file defines the Task model
'''
from django.db import models
from django.contrib.auth.models import User
PRIORITY_LEVELS = [
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
]
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority_level = models.CharField(
        max_length=2,
        choices=PRIORITY_LEVELS,
        default='M',
    )
    assignment = models.ForeignKey(User, on_delete=models.CASCADE)
    ending_date = models.DateTimeField()