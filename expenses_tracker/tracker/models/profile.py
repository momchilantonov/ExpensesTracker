from django.db import models
from expenses_tracker.tracker.models.expense import Expense


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()

    def budget_left(self):
        total_expenses_cost = sum(expense.price for expense in Expense.objects.all())
        return f'{self.budget-total_expenses_cost:.2f}'
