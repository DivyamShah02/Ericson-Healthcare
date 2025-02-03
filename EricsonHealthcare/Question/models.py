from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    VISIT_CHOICES = [
        ('hospital', 'hospital'),
        ('lab', 'lab'),
        ('chemist', 'chemist')
    ]
    visit_type = models.CharField(max_length=20, choices=VISIT_CHOICES)
