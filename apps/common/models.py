from django.db import models
import uuid

# Create your models here.

class TimeStampedUUIDModel(models.Model):
    pkid=models.BigAutoField(primary_key=True, editable=False)
    id=models.UUIDField(unique=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True