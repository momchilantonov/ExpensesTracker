from django.db import models
from expenses_tracker.tracker.models.expense import Expense


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()
    expenses = models.ForeignKey(
        Expense,
        on_delete=models.CASCADE,
    )
