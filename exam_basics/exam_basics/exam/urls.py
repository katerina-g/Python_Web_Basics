from django.urls import path

from exam_basics.exam.views import show_index, create_profile, delete_profile, profile_details, create_album, \
    album_details, album_edit, album_delete

urlpatterns = (
    path('', show_index, name='show index'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete', delete_profile, name='delete profile'),
    path('profile/details', profile_details, name='profile details'),
    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>', album_details, name='album details'),
    path('album/edit/<int:pk>', album_edit, name='album edit'),
    path('album/delete/<int:pk>', album_delete, name='album delete'),

)