from django.db import models
from expenses_tracker.tracker.models.expense import Expense


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()

    def budget_left(self):
        total_expenses = sum(exp.price for exp in Expense.objects.all())
        return self.budget-total_expenses
