from django.urls import path

from retake.retake_exam.views import show_home, create_profile, show_dashboard, create_game, game_details, game_edit, \
    game_delete, profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', show_home, name='show home'),
    path('dashboard', show_dashboard, name='dashboard'),
    path('game/create', create_game, name='create game'),
    path('game/edit/<int:pk>/', game_edit, name='edit game'),
    path('game/delete/<int:pk>/', game_delete, name='delete game'),
    path('game/details/<int:pk>/', game_details, name='game details'),
    path('profile/details/', profile_details, name='profile details'),
    path('create/profile/', create_profile, name='create profile'),
    path('edit/profile/', edit_profile, name='edit profile'),
    path('delete/profile/', delete_profile, name='delete profile'),
]
