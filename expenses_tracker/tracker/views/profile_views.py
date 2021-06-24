from django.shortcuts import render, redirect
from expenses_tracker.tracker.forms.profile_form import ProfileForm
from expenses_tracker.tracker.models import Profile, Expense
from expenses_tracker.tracker.views.common_views import show_form, save_form
from expenses_tracker.tracker.views.home_page_views import index


def profile_page(req):
    temp = 'profile.html'
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(req, temp, context)


def profile_edit_page(req):
    temp = 'profile-edit.html'
    red = index
    profile = Profile.objects.first()
    if req.method == "GET":
        profile_form = ProfileForm(initial=profile.__dict__)
        return show_form(req, profile_form, temp)
    profile_form = ProfileForm(
        req.POST,
        instance=profile,
    )
    return save_form(req, profile_form, temp, red)


def profile_delete_page(req):
    temp = 'profile-delete.html'
    red = index
    profile = Profile.objects.first()
    if req.method == "GET":
        return render(req, temp)
    profile.delete()
    for expense in Expense.objects.all():
        expense.delete()
    return redirect(red)
