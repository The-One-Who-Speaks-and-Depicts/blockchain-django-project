from django.db import models

class Block(models.Model):
	
	hash = models.CharField(name="Hash", max_length=255)
	height = models.IntegerField(name="Height")
	timestamp = models.IntegerField(name="Timestamp")
	transactions = models.IntegerField(name="Transactions")
	miner = models.CharField(name="Miner", max_length=255)

	def __str__(self):
		return str(self.Height)