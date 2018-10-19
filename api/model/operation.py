from django.db import models

from api.model.campaign import Campaign


class Operation(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name
