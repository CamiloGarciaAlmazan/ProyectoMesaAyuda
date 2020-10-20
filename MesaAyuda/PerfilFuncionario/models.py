from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
# Create your models here.

class Ticket(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200,help_text='resuma su problema')
    description= models.TextField(max_length=1000, help_text='explique a detalle su problema')
    status = models.CharField(max_length=200)

    def __str__(self):
	    return self.title
    
    def get_absolute_url(self):
	    """Returns the url to access a detail record for this book."""
	    return reverse('ticket-detail', args=[str(self.id)])

