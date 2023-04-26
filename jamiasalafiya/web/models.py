from django.db import models


class Result(models.Model):
    title = models.CharField(max_length=128)
    file = models.FileField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)
