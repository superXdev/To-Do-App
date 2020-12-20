from django.db import models
from django.utils import timezone

# Create your models here.
class ToDo(models.Model):
	date = models.DateTimeField()
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text
