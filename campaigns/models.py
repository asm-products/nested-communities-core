from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=200)
