from django.db import models

class Block(models.Model):
	
	hash = models.CharField(name="hash", max_length=255)
	height = models.IntegerField(name="height", primary_key=True)
	timestamp = models.IntegerField(name="timestamp")
	transactions = models.IntegerField(name="transactions")
	miner = models.CharField(name="miner", max_length=255)

	def __str__(self):
		return str(self.height)