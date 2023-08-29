"""
Definition of models.
"""

from django.db import models

# Create your models here.

# Create a class for Speaker with name, email and linkedin URL
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField()
    
def __str__(self):
    return self.name

# Create a class for Event with name, date, time, location, description, speaker and image
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    speaker = models.ForeignKey(Speaker, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/')
    
    # Create a field called code with a pattern of 3 letters, a dash and 3 numbers
code = models.CharField(max_length=7, unique=True, help_text='Format: ABC-123')
    
def __str__(self):
    return self.name



