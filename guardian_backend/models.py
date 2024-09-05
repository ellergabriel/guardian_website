from django.db import models

# Create your models here.
class Guardian(models.Model):
    fName = models.CharField(max_length = 60)
    lName = models.CharField(max_length = 60)
    