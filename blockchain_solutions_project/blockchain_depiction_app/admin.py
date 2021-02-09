from django.contrib import admin
from blockchain_depiction_app.models import Block

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
	pass
