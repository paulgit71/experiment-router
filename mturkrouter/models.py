from django.db import models

class MTurkLog(models.Model):
    mturk_id = models.CharField(max_length=64)
    country = models.CharField(max_length=64, blank=True, default="")
    region = models.CharField(max_length=64, blank=True, default="")      # Human label
    region_key = models.CharField(max_length=32, blank=True, default="")  # e.g., "LATIN"
    assigned_url = models.URLField(max_length=500, blank=True, default="")
    assigned_idx = models.PositiveSmallIntegerField(default=0)            # 0–5
    user_agent = models.TextField(blank=True, default="")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["mturk_id"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.mturk_id} @ {self.created_at:%Y-%m-%d %H:%M:%S}"
