from django.db import models 
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=255, help_text='Enter field name')
    email = models.EmailField()
    tagline = models.TextField(help_text='enter your tagline')
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.name 
    
class Address(models.Model):
    address = models.CharField(max_length=150)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    