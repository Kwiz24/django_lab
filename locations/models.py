from django.db import models
from companies.models import Company

class Location(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"
