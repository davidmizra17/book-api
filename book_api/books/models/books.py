from django.db import models
from model_utils.models import UUIDModel, TimeStampedModel


class Book(UUIDModel, TimeStampedModel):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=17, unique=True)
    cost_usd = models.DecimalField(decimal_places=2, max_digits=4)
    selling_price_local = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    category = models.CharField(max_length=30)
    supplier_country = models.CharField(max_length=30, null=True)