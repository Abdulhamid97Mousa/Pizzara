from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    path('<uuid:pk>/back/', views.back, name='back'),
    path('<uuid:project_id>/files/upload_file', views.upload_file, name='upload_file'),
    path('<uuid:project_id>/files/<uuid:pk>/delete/', views.delete_file, name='delete_file'),
    path('<uuid:project_id>/notes/add_note/', views.add_note, name='add_note'),  # Added trailing slash
    path('<uuid:project_id>/notes/<uuid:pk>/', views.note_detail, name='note_detail'),
    path('<uuid:project_id>/notes/<uuid:pk>/edit/', views.edit_note, name='edit_note'),
    path('<uuid:project_id>/notes/<uuid:pk>/delete/', views.delete_note, name='delete_note'),
    path('<uuid:project_id>/notes/back_note/', views.back_note, name='back_note'),
]