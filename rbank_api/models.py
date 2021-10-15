from django.db import models
from datetime import date

# Create your models here.
class Account(models.Model):
  today = date.today()
  owner = models.CharField(max_length=60)
  joint = models.CharField(blank=True, max_length=15)
  open_date = models.DateField(blank=True)

  def __str__(self):
    return self.owner