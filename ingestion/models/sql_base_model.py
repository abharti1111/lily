from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(db_index=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    meta_data = models.JSONField(null=True)
    