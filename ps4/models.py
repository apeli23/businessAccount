from django.db import models
from datetime import datetime

# Create your models here.
class Playstation(models.Model):
	income = models.IntegerField(default=0)
	expense = models.IntegerField(default=0)
	task_text = models.CharField(max_length=200)
	date_recorded = models.DateTimeField(default=datetime.now, blank=True)

