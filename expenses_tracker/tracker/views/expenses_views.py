from django.shortcuts import redirect
from expenses_tracker.tracker.models import Expense
from expenses_tracker.tracker.forms.expense_form import ExpenseForm
from expenses_tracker.tracker.views.common_views import show_form, save_form, get_id
from expenses_tracker.tracker.views.home_page_views import index


def expanse_create_page(req):
    temp = 'expense-create.html'
    red = index
    if req.method == "GET":
        expense_form = ExpenseForm()
        return show_form(req, expense_form, temp)
    expense_form = ExpenseForm(req.POST)
    return save_form(req, expense_form, temp, red)


def expense_edit_page(req, pk):
    temp = 'expense-edit.html'
    red = index
    expense = get_id(Expense, pk)
    if req.method == "GET":
        expense_form = ExpenseForm(initial=expense.__dict__)
        return show_form(req, expense_form, temp)
    expense_form = ExpenseForm(
        req.POST,
        instance=expense,
    )
    return save_form(req, expense_form, temp, red)


def expense_delete_page(req, pk):
    temp = 'expense-delete.html'
    red = index
    expense = get_id(Expense, pk)
    if req.method == "GET":
        expense_form = ExpenseForm(initial=expense.__dict__)
        for field in expense_form.fields.values():
            field.widget.attrs['disabled'] = True
        expense_form.save(commit=False)
        return show_form(req, expense_form, temp)
    expense.delete()
    return redirect(red)
