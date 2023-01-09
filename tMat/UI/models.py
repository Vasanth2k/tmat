from django.db import models

# Create your models here.
class PhaseOne(models.Model):
    target = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)