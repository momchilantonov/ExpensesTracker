from django.shortcuts import render

from expenses_tracker.tracker.models import Profile, Expense


def home_page(req):
    profile = Profile.objects.all()
    expenses = Expense.objects.all()
    context = {
        'profile': profile,
        'expenses': expenses,
    }
    if not profile:
        return render(req, 'home-no-profile.html', context)
    return render(req, 'home-with-profile.html', context)


def expanse_create_page(req):
    pass


def expense_edit_page(req, pk):
    pass


def expense_delete_page(req, pk):
    pass


def profile_page(req):
    pass


def profile_edit_page(req):
    pass


def profile_delete_page(req):
    pass


