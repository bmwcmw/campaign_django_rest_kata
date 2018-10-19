from django.db import models


class Campaign(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    read_only_name = models.CharField(
        max_length=255,
        null=True,
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.read_only_name)
