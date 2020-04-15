import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
	"""docstring for Task"""
	task_text=models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.task_text

	def was_published_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

class Accounts(models.Model):
	task=models.ForeignKey(Task, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	income = models.IntegerField(default=0)
	expense = models.IntegerField(default=0)
	balance = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
