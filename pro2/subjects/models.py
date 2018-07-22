from django.db import models

# Create your models here.
class Watch(models.Model):
    subject = models.CharField(max_length=128,null=True,blank=True)
    department = models.CharField(max_length=128, null=True,blank=True)
    link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True
    )
    def __str__(self):
        return self.subject
