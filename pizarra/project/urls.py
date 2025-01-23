from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    path('<uuid:pk>/back/', views.back, name='back'),
    path('<uuid:pk>/upload_file', views.upload_file, name='upload_file'),
    path('<uuid:project_id>/<uuid:pk>/delete/', views.delete_file, name='delete_file'),
]


# # Add this only in development (DEBUG=True)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)