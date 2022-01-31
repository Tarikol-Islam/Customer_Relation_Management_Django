from sys import maxsize
from tabnanny import verbose
from django.db import models
from django.forms import FloatField
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class MonthlyBenifit(models.Model):
    year = models.SmallIntegerField(verbose_name="Year", validators=([MaxValueValidator(9999),MinValueValidator(2000)]))
    month = models.SmallIntegerField(verbose_name="Month", validators=([MaxValueValidator(12),MinValueValidator(1)]))
    earnings = models.FloatField(verbose_name="Earning Track", default=0)

    class Meta:
        unique_together = ('year','month')

    def __str__(self) -> str:
        return ("Year("+str(self.year)+")-Month("+str(self.month)+")")