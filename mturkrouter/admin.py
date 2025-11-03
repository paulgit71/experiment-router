from django.contrib import admin
from .models import MTurkLog

@admin.register(MTurkLog)
class MTurkLogAdmin(admin.ModelAdmin):
    list_display = ("created_at","mturk_id","country","region","region_key","assigned_idx","ip_address")
    list_filter  = ("region_key","country","assigned_idx","created_at")
    search_fields = ("mturk_id","assigned_url","user_agent","ip_address")
    ordering = ("-created_at",)
