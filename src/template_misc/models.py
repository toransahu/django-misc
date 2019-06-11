from django.db import models

# Create your models here.


class Sample(models.Model):
    """Docstring for Sample. """
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    age = models.IntegerField(default=None, null=True)
