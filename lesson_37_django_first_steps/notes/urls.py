from django.urls import path

from . import views
# 0.0.0.0:8000/notes/...
urlpatterns = [
    path('', views.notes, name='notes'),
]