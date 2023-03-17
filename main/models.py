from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    quota_limit = models.IntegerField()
    quota_spent = models.IntegerField()


def __str__(Self):
    return self.name


class Translation(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
