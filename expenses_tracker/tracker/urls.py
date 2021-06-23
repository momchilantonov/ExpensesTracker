from django.urls import path
from expenses_tracker.tracker.views.home_page_views import index
from expenses_tracker.tracker.views.profile_views import profile_page, profile_edit_page, profile_delete_page
from expenses_tracker.tracker.views.expenses_views import expanse_create_page, expense_edit_page, expense_delete_page

urlpatterns = [
    path('', index, name='home page'),
    path('create/', expanse_create_page, name='expanse create page'),
    path('edit/<int:pk>', expense_edit_page, name='expense edit page'),
    path('delete/<int:pk>', expense_delete_page, name='expense delete page'),
    path('profile/', profile_page, name='profile page'),
    path('profile/edit/', profile_edit_page, name='profile edit page'),
    path('profile/delete/', profile_delete_page, name='profile delete page'),
]
