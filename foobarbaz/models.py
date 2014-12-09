from django.contrib.auth.models import User
from django.db import models

class ModelItem(models.Model):
    col1 = models.ForeignKey(User)
    col2 = models.CharField(max_length=15)
    col3 = models.CharField(max_length=15)
    col4 = models.DecimalField(max_digits=10, decimal_places=2)