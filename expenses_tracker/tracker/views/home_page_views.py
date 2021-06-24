from django.shortcuts import render
from expenses_tracker.tracker.models import Profile, Expense
from expenses_tracker.tracker.forms.profile_form import ProfileForm
from expenses_tracker.tracker.views.common_views import show_form, save_form


def home_page_with_profile(req):
    temp = 'home-with-profile.html'
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    context = {
        'profile': profile,
        'expenses': expenses,
    }
    return render(req, temp, context)


def home_page_without_profile(req):
    temp = 'home-no-profile.html'
    red = index
    if req.method == 'GET':
        profile_form = ProfileForm()
        return show_form(req, profile_form, temp)
    profile_form = ProfileForm(req.POST)
    return save_form(req, profile_form, temp, red)


def index(req):
    profile = Profile.objects.first()
    if profile:
        return home_page_with_profile(req)
    return home_page_without_profile(req)
