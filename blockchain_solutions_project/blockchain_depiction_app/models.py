from django.db import models

class Block(models.Model):
	
	hash = models.CharField(name="Hash", max_length=255)
	height = models.IntegerField(name="Height")
	version = models.IntegerField(name="Version")
	prevHash = models.CharField(name="PrevHash", max_length=255)
	nextHash = models.CharField(name="NextHash", max_length=255)
	merkleRoot = models.CharField(name="MerkleRoot", max_length=255)
	timestamp = models.IntegerField(name="Timestamp")
	bits = models.CharField(name="Bits", max_length=255)
	nonce = models.IntegerField(name="Nonce")
	hashStateRoot = models.CharField(name="HashStateRoot", max_length=255)
	hashUTXORoot = models.CharField(name="HashUTXORoot", max_length=255)
	prevOutStakeHash = models.CharField(name="PrevOutStakeHash", max_length=255)
	prevOutStakeN = models.IntegerField(name="PrevOutStakeN")
	signature = models.CharField(name="Signature", max_length=255)
	chainwork = models.CharField(name="Chainwork", max_length=255)
	flags = models.CharField(name="Flags", max_length=100)
	interval = models.IntegerField(name="Interval")
	size = models.IntegerField(name="Size")
	weight = models.IntegerField(name="Weight")
	transactions = models.JSONField(name="Transactions")
	miner = models.CharField(name="Miner", max_length=255)
	difficulty = models.FloatField(name="Difficulty")
	reward = models.IntegerField(name="Reward")
	confirmations = models.IntegerField(name="Confirmations")

	def __str__(self):
		return self.height