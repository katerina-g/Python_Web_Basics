from django.urls import path

from library.library_app.views import show_home, create_book, edit_book, show_details, show_profile, create_profile, \
    edit_profile, delete_profile, delete_book

urlpatterns = (
    path('', show_home, name='show home'),
    path('add/', create_book, name='create book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
