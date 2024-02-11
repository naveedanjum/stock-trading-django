from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    symbol = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'companies'

        indexes = [
            models.Index(fields=['name'], name='name_idx'),
        ]

    def __str__(self):
        return self.name + " ("+ self.symbol + ")"
