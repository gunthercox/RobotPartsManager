from django.db import models


class Robot(models.Model):
    name = models.CharField(max_length=20)
