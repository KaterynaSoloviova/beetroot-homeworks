from django.urls import path

from . import views

app_name = 'notes'
# 0.0.0.0:8000/notes/...
urlpatterns = [
    path('list/', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
